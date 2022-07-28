import unittest
from unittest.mock import patch
from src.services.rds_service import RDSService

class TestRdsService(unittest.TestCase):
    def setUp(self):
        self.host = 'jdbc:mysql://localhost:3306/teste'

    
    @patch('src.services.rds_service.RDS.get_connection')
    @patch('src.services.rds_service.RDS.get_endpoint_url')
    def test_get_connection(self, mock_get_endpoint_url, mock_get_connection):
        mock_get_endpoint_url.return_value = 'https://rds.sa-east-1.amazonaws.com/123456789012'
        mock_get_connection.return_value = {
            'Connection': 'teste'
        }
        rds = RDSService()
        response = rds.get_connection(self.host)['Connection']
        self.assertEqual(response, 'teste')