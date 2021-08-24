from src.consistencia_parametros import ConsistenciaParametros
from src.consulta_carros_dynamo import ConsultaCarrosDynamo


class Controller:
    def __init__(self, event):
        self.event = event
        self.resource = event.get('resource')
        self.path = event.get('path')
        self.httpmetod = event.get('httpMethod')
        self.querystringparameters = event.get('queryStringParameters')
        # print('Parametros de entrada')
        # print(self.event)
        # print(self.resource)
        # print(self.path)
        # print(self.httpmetod)
        # print(self.querystringparameters)
        # print('-------------------')
        self.paths = {
            'follow_up': ('/consulta-carros-aws/v1/placas')
        }

    def executa(self):
        if self.httpmetod == 'GET':
            if self.path == self.paths.get('follow_up'):
                # print('PATHS')
                # print(self.path)
                # print(self.paths.get('follow_up'))
                # print('-------------------')
                consistencia = ConsistenciaParametros(
                    self.querystringparameters
                )

                # Faz a validação, e se inconsistente devolve uma string do erro
                resultado_consistencia = consistencia.consistencia()
                print('Resultado consistencia')
                print(resultado_consistencia)
                print('-------------------')

                # Se o Retorno nao estiver vazio ele imprime a excecao
                if (len(resultado_consistencia) != 0):
                    raise Exception(resultado_consistencia)

                follow_up = ConsultaCarrosDynamo(self.querystringparameters)
                resultado_consulta = follow_up.consulta()
                print('Resultado consulta: ')
                print(resultado_consulta)
                print('-------------------')
                return resultado_consulta
        return "{}"
