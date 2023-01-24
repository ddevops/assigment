* Tool introduction/explanation

A python based tool which consumes messages from SQS and write them to DynamoDB. It is also responsible for deltion of items in DB.

* How to build the tool and build requirements

Run the tool by python3 program.py

How to configure the environment (if necessary)

Start localstack environment (awslocal can be aliased to: "alias al='awslocal --endpoint-url=http://localhost:4576 --region=ap-southeast-1'")
Run message_genrator
RUN the tool
and execute the command you require

How to run the tool

python3 program.py

How to use the tool (options, parameters, etc.)

Once the program is started. You'll be asked to provide input. Following inputs are supported:
- consume --count n
- show
- clear

Challenges while solving the problem

First challenge was to resolve the localstack port, so the message generator can connect to it
Setting up awslocal to use specific endpoint and region

Note: currently duplicates are not being handled by this application and dupliates may occur.
Also I would have like to work on Bonus points as they are also mainly the devops related tasks
but currently due to limited time left I couldn't work on it.