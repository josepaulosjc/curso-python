#!python
# ----------- Exercício: Manipulacão CSV com Stream e With----------- #

# Nesse exemplo o 'With' abre um arquivo, atribui uma variável e fecha automaticamente após a operação
with open('manipulacao_arquivos\pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O Arquivo foi fechado!')
