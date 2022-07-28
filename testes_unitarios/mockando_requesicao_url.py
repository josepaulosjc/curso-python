import unittest
from unittest.mock import patch
from src.services.sqs_service import SQSService


class TestSQSService(unittest.TestCase):
    def setUp(self):
        self.sqs_service = SQSService()

    @patch('src.services.sqs_service.SQS.get_queue_url')
    @patch('src.services.sqs_service.SQS.send_message')
    def test_send_message(self, mock_send_message, mock_get_queue_url):
        mock_send_message.return_value = {
            'MessageId': '12345678901234567890123456789012',
            'ResponseMetadata': {
                'HTTPStatusCode': 200
            }
        }
        mock_get_queue_url.return_value = 'https://sqs.sa-east-1.amazonaws.com/123456789012/teste'
        sqs = SQSService()
        response = sqs.send_message('teste', 'teste')['ResponseMetadata']['HTTPStatusCode']
        self.assertEqual(response, 200)