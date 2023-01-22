import boto3
import json

endpoint_url = "http://localhost:4576"
region_name = "ap-southeast-1"

iam = boto3.client('iam', endpoint_url=endpoint_url, region_name=region_name)

role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:ap-southeast-1:000000000000:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:ap-southeast-1:000000000000:log-group:/aws/lambda/lambdaSqsDynamo:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:Scan",
                "dynamodb:UpdateItem"
            ],
            "Resource": "arn:aws:dynamodb:ap-southeast-1:000000000000:table/message"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueAttributes",
                "sqs:ReceiveMessage"
            ],
            "Resource": "arn:aws:sqs:ap-southeast-1:000000000000:test-queue"
        }
    ]
}

response = iam.create_role(
  RoleName='LambdaSqsDynamoRole',
  AssumeRolePolicyDocument=json.dumps(role_policy),
)
print(response)