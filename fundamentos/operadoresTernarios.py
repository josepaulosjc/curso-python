esta_chovendo = True

# Composição
#('F','V')[expressao]
#('Se for diferente','Se for igual')[expressao]

# 1a Forma
print('Minhas roupas estao ' + ( 'secas' , 'molhadas')[esta_chovendo])

# 2a Forma
print('Minhas roupas estao ' + ( 'molhadas' if esta_chovendo else 'secas' ))