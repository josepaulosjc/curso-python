#! python
# ----------- Exercício - Exceções com de arquivo com parâmetros ----------- #

from math import pi
import sys
import errno


class TerminalColor:
    # Cores, ERRO = vermelho, NORMAL = branca
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print('É necessário informar o raio do circulo.')
    print('Sinaxe: {} <raio>'.format(sys.argv[0]))


if __name__ == '__main__':
    # Se argv menor que 2, o parâmentro não foi passado.
    if len(sys.argv) < 2:
        help()
        # errno.EPERM - O mesmo que 1,  1 - Erro e sai do arquivo, 0 - Sucesso e sai do arquivo.
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO +
              'O raio deve ser um valor numérico' + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo', area)
