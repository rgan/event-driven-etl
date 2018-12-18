import json

from mockito import verify, never, any

from log_processor import LogProcessor
from message import Message
from tests.base_test_case import BaseTestCase


class LogProcessorTest(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.log_processor = LogProcessor(self.topic_arn, self.queue_url)

    def test_should_process_log_collected_messages(self):
        log_msg = json.dumps({"type": "batch_collected", "batch_id": "20181201"})
        msg = json.dumps({"Message": log_msg})
        self.log_processor.process_message(Message(msg))
        msg_json = {"type": "batch_processed", "batch_id": "20181201"}
        verify(self.sns_service_mock).publish(TopicArn=self.topic_arn,
                Message=json.dumps(msg_json))

    def test_should_not_process_other_messages(self):
        log_msg = json.dumps({"type": "batch_processed", "batch_id": "20181201"})
        msg = json.dumps({"Message": log_msg})
        self.log_processor.process_message(Message(msg))
        verify(self.sns_service_mock, never).publish(TopicArn=self.topic_arn,
                Message=any())