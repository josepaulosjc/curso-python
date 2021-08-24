import json
import boto3

# Recuperando Toda a Tabela #

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    data = client.scan(
        TableName='carros'
    )
    response = {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    return response
