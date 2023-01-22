import boto3

endpoint_url = "http://localhost:4576"
region_name = "ap-southeast-1"

# Choosing the resource from boto3 module
sqs = boto3.resource('sqs', endpoint_url=endpoint_url, region_name=region_name)

# Get the queue named test
queue = sqs.get_queue_by_name(QueueName='test-queue')

# Process messages by printing out body from test Amazon SQS Queue
for message in queue.receive_messages():
    print('message = {0}'.format(message.body))
    message.delete()

# Print out each queue name, which is part of its ARN
#for queue in sqs.queues.all():
#    print(queue.url)