import math


def calcular_baskara(a, b, c):
    #a = input('Entre com o valor de A: ')
    #b = input('Entre com o valor de B: ')
    #c = input('Entre com o valor de C: ')
    return print(f'{baskara(float(a), float(b), float(c))}')


def baskara(*valores):
    lista = calc_raizes(delta(*valores), *valores)
    return lista


def delta(a, b, c):
    return b**2 - 4 * a * c


def calc_raizes(delta, a, b, c):
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        return (-b + math.sqrt(delta)) / (2*a)
    else:
        return f'A equacao nao possui raizes, Delta = {delta}'


if __name__ == '__main__':
    a, b, c = 5, 1, 6
    print('Calculando a Formula de Baskara...')
    calcular_baskara(a, b, c)
