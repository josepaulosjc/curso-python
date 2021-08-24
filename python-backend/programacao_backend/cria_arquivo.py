import json

# ----------- Gravando JSON -----------#
try:
    arq = open('python-backend/programacao_backend/teste_escrita.json', 'w')
    arq.write('{"nome": "Jose", "idade": 29}')
    arq.close()
except:
    print('Não foi possível escrever o arquivo.')


try:
    arq2 = open('python-backend/programacao_backend/teste_escrita.json')
    pessoa = arq2.read()
    print(pessoa)
    arq2.close()
except:
    print('Não foi possível ler o arquivo.')


# ----------- Lendo JSON -----------#
try:
    arq3 = open('python-backend/programacao_backend/teste_escrita.json', 'r')
    lista = json.load(arq3)
    print(lista['nome'])
    arq3.close()
except:
    print('Não foi possível ler o arquivo!')
