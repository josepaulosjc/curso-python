class Dados:
    def __init__(self, dados={}):
        self.nome = dados.get('nome')
        self.sobrenome = dados.get('sobrenome')
        self.idade = dados.get('idade')
        self.endereco = dados.get('endereco')
        self.profissao = dados.get('profissao')

    def funcao_ignorada(self):
        pass

    def formatar(self):
        atributos = filter( lambda a: not a.startswith('__') and 
            not callable(getattr(self, a)), dir(self))

        for attr in atributos:
            if self.__getattribute__(attr) in [None,'null','']:
                self.__setattr__(attr, 'lala')

        return self.__dict__


if __name__=='__main__':

    dados = {
        'nome':'Jose',
        'idade': 29,
        'sobrenome':'Amancio',
        'endereco':'Avenida Dois',
        'profissao':'Analista'
    }

pessoa = Dados(dados)
print(pessoa.formatar())
