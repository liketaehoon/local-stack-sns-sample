import os
import boto3
from functions.main.sns.sns_basics import SnsWrapper

def main(event, context):
    ENV = os.environ["stage"]
    print('# ENV = ' + ENV)
    if 'Records' in event:
        for record in event['Records']:
            print(record['Sns']['Message'])
            print(record['Sns']['MessageAttributes'])
    return {}

def trigger(event, context):
    print ("trigger exeucted")
    wrapper = SnsWrapper(boto3.resource('sns',
                              use_ssl=False,
                              endpoint_url="http://localhost:4566"))
    topics = wrapper.list_topics()
    for topic in topics:
        print(topic)
        wrapper.publish_message(topic, 'hello from local-stack-sns-sample', { "status": "completed" })
        print("message published")
    return {}