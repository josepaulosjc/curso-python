#!python
# ----------- Exercício: Escrevendo CSV com Stream e With----------- #

with open('manipulacao_arquivos\pessoas.csv') as arquivo:
    # With(arquivo, módulo) - w = write(escrita)
    with open('manipulacao_arquivos\pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # file=saida ---> grava a saida no arquivo
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('O Arquivo foi fechado!')

if saida.closed:
    print('O Arquivo foi gerado!')
