import boto3


class ConsultaCarrosDynamo:
    def __init__(self, params={}):
        self.placa = params.get('placa')
        self.ano = params.get('ano')
        self.modelo = params.get('modelo')
        self.table = boto3.resource('dynamodb').Table('carros')
        self.tipo_consulta = params.get('tipo_consulta')

    # def consulta(self):
    #     params = {'placa': self.placa}
    #     resultquery = self.table.get_item(Key=params)
    #     return self.extrai_dados_consulta(resultquery)

    def consulta_carro_placa(self):
        params = {'placa': self.placa}
        resultquery = self.table.get_item(Key=params)
        return self.extrai_dados_consulta(resultquery)

    def consulta(self):
        resultado = {
            "1": lambda: self.consulta_carro_placa(),
            "2": lambda: self.consulta_carro_cor(),
            "3": lambda: self.consulta_carro_ano_modelo()
        }

        return resultado.get(self.tipo_consulta,
                             lambda: "ERROR: Tipo de consulta não é válido.")()

    def extrai_dados_consulta(self, resultquery):
        # list_carros = [] Tranformas em lista depois
        print('Extrai dados consulta: ')
        print(resultquery)
        return resultquery
