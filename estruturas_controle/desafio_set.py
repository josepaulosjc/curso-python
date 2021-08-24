PALARAS_PROIBIDAS = {'futebol', 'religiao', 'politica'}

textos = [
    'Joao gosta de futebol e politica.',
    'A praia foi divertida.'
]

for texto in textos:
    intersecao = PALARAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui pelo menos uma palavra proibida.', intersecao)
    else:
        print('Texto autorizado.', texto)
