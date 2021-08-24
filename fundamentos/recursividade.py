# Imprime um certa quantidade de vezes
def imprimir(maximo, atual):
    if atual >= maximo:
        return
    imprimir(maximo, atual + 1)


imprimir(10, 1)
