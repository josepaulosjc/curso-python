from src.controller import Controller
import json

'''
{
    "resource": "123",
    "httpMethod": "GET",
    "path":"/consulta-carros-aws/v1/placas",
    "queryStringParameters": {
        "placa" : "xpto215",
        "tipo_consulta" : "1"
    }
}
'''


def lambda_handler(event, context):
    try:
        controller = Controller(event)  # Instancia Controlador
        return_result_dynamo = controller.executa()  # Obtem Resultado da Consulta
        print('Retorno da Consulta')
        print(return_result_dynamo)
        print('-------------------')

        if return_result_dynamo == []:
            response = {
                "statusCode": 404,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "status ": "Nao encontrado "
                })
            }
        else:
            response = {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps(return_result_dynamo)
            }
        return response

    except Exception as e:
        print('Erro execucao lambda handler.')
        print(e)
        print('-------------------')

        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "status ": f"Nao encontrado {str(e)}"
            })
        }
