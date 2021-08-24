def calcular(valor, taxa, prazo):
    juros = valor * (taxa/100) * prazo
    montante = valor + juros
    return juros, montante


j, m = calcular(1000.00, 2.5, 10)
print(j, m)
