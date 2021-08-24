def multiplicar(x):  # Uma funcao dentro de outra, indica 'Alta Ordem'
    def calcular(y):  # Calcular já reconhece 'X' definido em 'multiplicar' conceito de Closure
        return x * y
    return calcular  # Retorna Calcular com o X já armazenado anteriormente, alta ordem


if __name__ == '__main__':
    dobro = multiplicar(2)  # X = 2, e prepara a funcao calcular
    triplo = multiplicar(3)  # X = 3, e prepara a funcao calcular
    #print(dobro, triplo)
    print(f'O triplo de 3 eh {triplo(3)}')  # calcular, recebe Y = 3
    print(f'O dobro de 5 eh {dobro(5)}')  # calcular, recebe Y = 5

    print(f' 5 x 7 = {multiplicar(5)(7)}')  # Passagem de dois parâmetros
