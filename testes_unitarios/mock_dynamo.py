item1 = {
    "campo1": "valor1",
    "campo2": "valor2",
    "campo3": "valor3",
}
item2 = {
    "campo1": "valor1",
    "campo2": "valor2",
    "campo3": "valor3",
}

def dy_client(dynamodb):

    table = dynamo.create_table(
        TableName='teste',
        KeySchema=[
            {
                "AttributeName": "campo1",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "campo1",
                "AttributeType": "S"
            },
            {
                "AttributeName": "campo2",
                "AttributeType": "S"
            },{
                "AttributeName": "campo3",
                "AttributeType": "S"
            }
        ],
        GlobalSecondaryIndexes=[{
            "IndexName": "xcd0000",
            "KeySchema": [
                {
                    "AttributeName": "campo2",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "campo3",
                    "KeyType": "RANGE"
                }],
                "Projection": {
                    "ProjectionType": "ALL"
                },
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1
                }
        }],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName='teste')
    assert table.item_status == 'ACTIVE'

    table.put_item(Item=item1)
    table.put_item(Item=item2)

    return table
    