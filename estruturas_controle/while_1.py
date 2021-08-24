# while True:
#   print('Laço infinito...')

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o numero secreto...'))

    if -1 != numero_informado != numero_secreto:
        print('O número não é esse, por favor tente novamente.')

print(
    f'Parabéns!!! Você acertou o número. O numero secreto é {numero_secreto}!')
