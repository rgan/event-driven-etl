import argparse
import json
import logging

import boto3

from message import Message


class BaseProcessor:

    def __init__(self, topic_arn, queue_url):
        self.sns = boto3.client('sns')
        self.sqs = boto3.resource('sqs')
        self.topic_arn = topic_arn
        self.queue_url = queue_url

    # subclasses implement this method
    # return True if message was handled, else False
    def process_message(self, msg):
        return False

    def publish(self, msg_json):
        # cannot fail here since message.delete() won't be called for the
        # message that triggered this processing
        try:
            self.sns.publish(
                TopicArn=self.topic_arn,
                Message=json.dumps(msg_json)
            )
        except:
            logging.critical("Could not publish {0} to SNS topic".format(msg_json))

    def process(self):
        queue = self.sqs.Queue(self.queue_url)
        for message in queue.receive_messages():
            logging.info(message.body)
            if self.process_message(Message(message.body)):
                # Let the queue know that the message is processed
                message.delete()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('topicArn', help='AWS SNS topic ARN to subscribe to for notifications')
    parser.add_argument('queueUrl', help='AWS SQS queue for receiving notifications')
    args = parser.parse_args()
    logging.basicConfig(filename='log_processor.log', level=logging.DEBUG)
    return args
