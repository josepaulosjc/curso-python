#!python
# ----------- Exercício: Manipulacão CSV com Stream e Try / Finaly----------- #

try:
    arquivo = open('manipulacao_arquivos\pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

finally:
    arquivo.close()

if arquivo.closed():
    print('O Arquivo foi fechado!')
