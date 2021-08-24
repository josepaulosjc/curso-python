#!python
# ----------- Exercício: Manipulacão CSV e Split ----------- #

arquivo = open('manipulacao_arquivos\pessoas.csv')
# Lê todo arquivo e depois manipula, exemplo 5mb de dados.
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
