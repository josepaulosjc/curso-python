from datetime import datetime
import re

class ConsistenciaParametros:
    def __init__(self, parametros):
        self.id = parametros.get('id')
        self.name = parametros.get('name')
        self.erros = []

    def consistencia(self):
        funcoes = [self.validar_id, 
                    self.validar_name]
        result = list(filter(lambda valor: valor != '', map(
            lambda funcao: funcao(), funcoes))
            )
        return result


    def validar_id(self):
        regex = re.compile('[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}\Z')
        if self.id is None:
            return 'id não informado'
        elif not regex.match(self.id):
            return 'id inválido'
        return ''
    
    def validar_name(self):
        if self.name is None:
            return 'name não informado'
        return ''


consistencia = ConsistenciaParametros(id='12345678-1234-1234-1234-123456789012', name='Teste')
result = consistencia.consistencia()
if result != []:
    print('Erro consistencia')
    raise Exception('Erro consistencia', result)
else:
    print('Consistencia ok')