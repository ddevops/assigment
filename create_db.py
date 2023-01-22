import boto3

endpoint_url = "http://localhost:4576"
region_name = "ap-southeast-1"

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url, region_name=region_name)

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='message',
    KeySchema=[
        {
            'AttributeName': 'body',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'body',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
print(table)