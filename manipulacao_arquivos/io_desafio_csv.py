#!python

import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        # Converte o arquivo na codificação correta
        dados = entrada.read().decode('latin1')
        print('Download Completo!')
        for cidade in csv.reader(dados.splitlines()):  # Quebra o arquivo em linhas
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
