def fatoracao(numero):
    generator = (i for i in range(2, numero + 1) if numero % i == 0)
    divisor = next(generator)
    fatores = []

    while numero / divisor != 1:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero = numero / divisor
        else:
            divisor = next(generator)
    fatores.append(divisor)
    return fatores


if __name__ == '__main__':
    print(f'{fatoracao(500)}')
