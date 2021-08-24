import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dadosobtidos = False
    
    def obter_todos_os_dados(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if resposta.ok:
            self.dadosobtidos = True
            return 'CONECTADO'
        
        else:
            self.dadosobtidos = False
            return 'ERRO 404'