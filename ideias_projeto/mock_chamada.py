import requests
import unittest
from unittest.mock import patch
from src.service.request_api_data import RequestApiData as api

class TestDatabaseFunctions(unittest.TestCase):

    @patch('src.service.request_api_data.RequestApiData.get_token_acess')
    def test_get_token_acess_OK(self, mock_get):
        mock_get.return_value.status_code = 200
        response = api.get_token_acess()
        self.assertEqual(reresponse.status_code, 200)

    @patch('src.service.request_api_data.RequestApiData.get_token_acess')
    def test_get_token_acess_NOK(self, mock_get):
        mock_get.return_value.status_code = 400
        api.client_id = ""
        response = api.get_token_acess()
        self.assertEqual(reresponse.status_code, 400)