import os
import boto3
import unnitest
from unittest.mock import MagicMock
from moto import mock_dynamodb2

@mock_dynamodb2
class TestDynamo(unnitest.TestCase):
    def setUp(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')
        self.table = dynamo_table_test.dy_client(self.dynamodb)

    def tearDown(self):
        self.table.delete()
        self.dynamodb = None

    def test_table_exists(self):
        self.assertTrue(self.table.exists())
        self.assertIn('teste', self.dynamodb.table.name) # Verifica se a tabela existe com mesmo nome

    def test_consulta(self):
        self.query = {
            "campo1": "valor1",
            "campo2": "valor2"
        }

        consulta = ConsultaBanco(self.query)
        consulta.consulta = MagicMock(return_value=True)
        objeto = consulta.consulta()
        consulta.consulta.assert_called_once_with()
        self.assertEqual(objeto['campo1'], 'valor1')