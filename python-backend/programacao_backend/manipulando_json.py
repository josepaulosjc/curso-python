# ----------- Manipulando JSON -----------#
import json

''' EXEMPLO JSON
{
    "nome": "Fulano",
    "idade": 90,
    "filmes_preferidos": [ "Pulp Fiction", "Clube da Luta" ],
    "contatos": {
        "telefone": "(11) 91111-2222",
        "emails": [ "fulano@gmail.com", "fulano@yahoo.com" ]
    }
}
'''

# Lendo arquivo Json
arq = open('python-backend/programacao_backend/teste_escrita.json')
pessoa = arq.read()
arq.close()

print(pessoa)
print(type(pessoa))

# Convertendo str em json
obj = json.loads(pessoa)
print(obj['nome'])

# Percorrendo Json
for filme in obj['filmes_preferidos']:
    print(filme)

# Percorrer as chaves e valores do objeto "contatos"
for tipo, contato in obj['contatos'].items():
    print('{}={}'.format(tipo, contato))

# Incluir um novo contato
obj['contatos']['twitter'] = '@fulano'

# imprimir o json (indentando com 2 espaços)
print(json.dumps(obj, indent=2))


# ----------- DUMP e DUMPS ----------#

dados = {
    "nome": "Renato Lelis",
    "profissao": "Desenvolvedor de sistemas"
}

with open('dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)

dados_json = json.dumps(dados)

print(type(json_file))
print(type(dados_json))

# ----------- LOAD e LOADS ----------#

with open('dados.json', 'r') as json_file:
    dados = json.load(json_file)
    print(dados)
    print(type(dados))

    # {'nome': 'Renato Lelis', 'profissao': 'Desenvolvedor de sistemas'}
    # # <class 'dict'>

dados = '{"nome": "Renato Lelis","profissao": "Desenvolvedor de sistemas"}'
dados_json = json.loads(dados)
print(type(dados_json))
# <class 'dict'>
