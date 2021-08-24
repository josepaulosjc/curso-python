import json
import boto3

# Recuperando um item da Tabela #

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table = dynamodb.Table('carros')
    try:
        response = table.get_item(Key={'placa': event['placa']})
    except:
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "status ": "Nao encontrado "
            })
        }
    else:
        return response['Item']
