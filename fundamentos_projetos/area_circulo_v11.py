#! python
# ----------- Exercício: Validação de arquivo com parâmetros ----------- #

from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # Se argv menor que 2, o parâmentro não foi passado.
    if len(sys.argv) < 2:
        print('É necessário informar o raio do circulo.')
        print('Sinaxe: {} <raio>'.format(sys.argv[0]))
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo', area)
