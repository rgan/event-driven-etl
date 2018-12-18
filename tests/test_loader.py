import json

from mockito import verify

from loader import Loader
from message import Message
from tests.base_test_case import BaseTestCase


class LoaderTest(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.loader = Loader(self.topic_arn, self.queue_url)

    def test_should_process_log_processed_messages(self):
        log_msg = json.dumps({"type": "batch_processed", "batch_id": "20181201"})
        msg = json.dumps({"Message": log_msg})
        self.loader.process_message(Message(msg))
        msg_json = {"type": "batch_loaded", "batch_id": "20181201"}
        verify(self.sns_service_mock).publish(TopicArn=self.topic_arn,
                Message=json.dumps(msg_json))

