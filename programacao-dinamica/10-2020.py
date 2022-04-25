with open('input.txt') as file:
    adaptadores = file.read().splitlines()
    adaptadores = list(map(int, adaptadores))

# PART 1
adaptadores.sort()
adaptadores.append(adaptadores[-1] + 3)
qtdDiferencas1 = 0
qtdDiferencas3 = 0
ultimoAdaptador = 0
for adaptador in adaptadores:
    if adaptador - ultimoAdaptador == 1:
        qtdDiferencas1 += 1
    elif adaptador - ultimoAdaptador == 3:
        qtdDiferencas3 += 1
    ultimoAdaptador = adaptador

print(qtdDiferencas1 * qtdDiferencas3)


# PART 1 - Programação Dinâmica
qtdDiferencas = {}
ultimoAdaptador = 0
for adaptador in adaptadores:
    
    diferenca = adaptador -ultimoAdaptador      # 1 - ver a diferença
    if diferenca in qtdDiferencas:                    # 2 - verificar se já foi contabilizado
        qtdDiferencas[diferenca] += 1           # 3 - incrementa a quantidade no dict
    else:
        qtdDiferencas[diferenca] = 1            # 4 - se não, adiciona um novo valor no dicionario
    
    ultimoAdaptador = adaptador

print(qtdDiferencas)                            # 5 - {1: 75, 3: 33} Lê se, 75 diferencas do tipo 1 e 33 diferencas do tipo 3
print(qtdDiferencas.get(1) * qtdDiferencas.get(3))