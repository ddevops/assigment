Q1: Please explain what is the advantage of using SQS in this solution.

Message Queues helps when working with distributed applications and reduce coding complexcity for decupled 
components. In current application SQS is being used to produce message coming from the message generator script, 
thus it can be consumed later by the consumer script and moved to dynamodb.

Q2: Compare SQS to a message broker you have used before. What are the differences? Strong/weak points? (If you
did not use such a solution, please skip this question)

I have previously worked with RabbitMQ on the local VM setup. Where the producer application is responsible to 
publish messages on the queues and a consumer application is processing messages from the queue. In case you have
requirement to work on the VM setup out of any public cloud provider, rabbitmq is on of the message broker 
application which can be used. As a weak point you need to manage such RMQ cluster by yourself.

Q3: If we run multiple instances of this tool, what prevents a message from processed twice?

Once the message is consumed from SQS it is pushed to dynamoDB and removed from queue.

Q4: In very rough terms, can you suggest an alternative solution aside from using SQS from your previous experience
using different technologies?

Using Amazon MQ/Rabbitmq message broker services can be an alternate for using SQS in AWS managed stack. One of the 
other option which can be used is Apache Kafka. Kafka provides high throughput to manage streams data and is also
reliable data source. Kafka works on pull based approach and RMQ works as push based.