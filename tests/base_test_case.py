import unittest

import boto3
from mockito import mock, when

from log_processor import LogProcessor


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.sns_service_mock = mock()
        when(boto3).client('sns').thenReturn(self.sns_service_mock)
        self.sqs_service_mock = mock()
        when(boto3).client('sqs').thenReturn(self.sqs_service_mock)
        self.topic_arn = "test_topic_arn"
        self.queue_url = "test_queue_url"

