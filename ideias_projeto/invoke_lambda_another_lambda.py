import json
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    logger.info('event: {}'.format(json.dumps(event)))

    inputParams = {
        "ProductName": "Widget",
        "Quantity": 10,
        "UnitPrice": 1.23
    }

    response = client.invoke(
        FunctionName='lambda_another_lambda',
        InvocationType='RequestResponse',
        Payload=json.dumps(inputParams)
    )

    responseFromChild = json.loads(response['Payload'].read().decode('utf-8'))
    return responseFromChild