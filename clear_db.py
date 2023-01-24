import boto3

endpoint_url = "http://localhost:4576"
region_name = "ap-southeast-1"

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url, region_name=region_name)

# Choose DynamoDB table
table = dynamodb.Table('message')

def clear():
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(
                Key={
                    'body': each['body']
                }
            )
    print("db cleared")

if __name__ == "__clear__":
    clear()