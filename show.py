import boto3

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

def show():
    # Consume all messages from queue
    while True:
        response = client.receive_message(
            QueueUrl="http://localhosts:4576/000000000000/test-queue",
            MaxNumberOfMessages=1,
            WaitTimeSeconds=1,
        )
            
        for message in response.get("Messages",[]):
            message_body = message["Body"]

        if len(response.get('Messages',[])) == 0:
            break

        else:
            print(message_body)

if __name__ == "__show__":
    show()