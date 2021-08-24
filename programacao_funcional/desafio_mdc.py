def mdc(numeros):   # lista de numeros
    def calc(divisor):  # candidato a divisor
        # Se o elemento % iterador == 0, ele soma com o proximo
        # Pega todos os numero que somados o resto é 0
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor - 1)
    return calc(min(numeros))


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1'''
