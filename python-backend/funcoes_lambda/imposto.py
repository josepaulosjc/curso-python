preco = 1000

# ---- Funcao Comum ----- #


def calcular_imposto_normal(preco):
    return preco * 0.3


print(calcular_imposto_normal(preco))

# ---- Funcao Lambda ----- #
#calcular_imposto = lambda preco : preco* 0.3


def calcular_imposto(preco): return preco * 0.3


precos = [100, 500, 10, 25]
impostos = list(map(lambda x: x * 0.03, precos))
print(impostos)
