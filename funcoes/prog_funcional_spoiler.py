# --------- Callable --------- #

def executar(funcao):
    if callable(funcao):    # Callable verifica se o item passado pode ser chamado como uma função
        funcao()


def bom_dia():
    print('Bom dia!')


def boa_tarde():
    print('Boa tarde!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    # Não acontece nada porque '1' não pode ser executado como uma função
    executar(1)
