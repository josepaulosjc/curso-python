def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))

    # Fazendo o Packing - pega os número e empacota eles soma_n(*numeros)
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 1, 1, 1, 1, 1, 1))

    # Fazendo o Unpacking - pega os número e empacota eles 'soma_n(*numeros)'
    tupla_nums = (1, 2, 3)          # Atribui em uma variavel
    print(soma_3(*tupla_nums))      # Desempacota a variavel 'soma_3(a, b, c)'
    lista_nums = [1, 2, 3]
    print(soma_3(*lista_nums))
