import boto3
import json

endpoint_url = "http://localhost:4576"
region_name = "ap-southeast-1"

# Choosing the resource from boto3 module
sqs = boto3.resource('sqs', endpoint_url=endpoint_url, region_name=region_name)
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url, region_name=region_name)
client = boto3.client('sqs', endpoint_url=endpoint_url, region_name=region_name)

# Choose DynamoDB table
table = dynamodb.Table('message')

# Get the queue named test
queue = sqs.get_queue_by_name(QueueName='test-queue')

# Consume all messages from queue
def consumer(c):
    i=0
    while i<c:
        # Process messages by printing out body from test Amazon SQS Queue
        for message in queue.receive_messages():
                print('message = {0}'.format(message.body))
                table.put_item(
                    Item={
                    'body': format(message.body),
                })
                message.delete()
                i=i+1