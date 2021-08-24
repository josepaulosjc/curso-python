#!python
# ----------- Exercício: Manipulacão CSV com Stream ----------- #
# Nesse exemplo ele lê o arquivo sob demanda, com o Stream

arquivo = open('manipulacao_arquivos\pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
