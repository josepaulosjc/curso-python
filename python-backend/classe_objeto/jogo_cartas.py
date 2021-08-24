from random import randint


class Baralho:
    naipe = ['ouros', 'paus', 'espadas', 'copas']

    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = self.naipe[naipe]

    def mostra_carta(self):
        return f' Carta {self.numero} de {self.naipe}'


jogador1 = Baralho(numero=randint(1, 14), naipe=randint(0, 3))
jogador2 = Baralho(numero=randint(1, 14), naipe=randint(0, 3))

print(f'Jogador 1: {jogador1.mostra_carta()}')
print(f'Jogador 2: {jogador2.mostra_carta()}')

if jogador1.numero > jogador2.numero:
    print(f'Jogador 1: Ganhou')
if jogador1.numero < jogador2.numero:
    print(f'Jogador 2: Ganhou')
elif jogador1.numero == jogador2.numero:
    print(f'A jogada terminou em empate!')
