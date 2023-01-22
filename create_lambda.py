import boto3

endpoint_url = "http://localhost:4576"
region_name = "ap-southeast-1"

iam_client = boto3.client('iam', endpoint_url=endpoint_url, region_name=region_name)
lambda_client = boto3.client('lambda', endpoint_url=endpoint_url, region_name=region_name)

with open('sqs-lambda-dynamodb-java.zip', 'rb') as f:
	zipped_code = f.read()
  
role = iam_client.get_role(RoleName='LambdaSqsDynamoRole')

response = lambda_client.create_function(
    FunctionName='SQStoDynamoDB',
    Runtime='java11',
    Role=role['Role']['Arn'],
    Handler='handler.lambda_handler',
    Code=dict(ZipFile=zipped_code),
    Timeout=300, # Maximum allowable timeout
    # Set up Lambda function environment variables
    Environment={
        'Variables': {
            'Name': 'SQStoDynamoDB'
        }
    },
)
print(response)