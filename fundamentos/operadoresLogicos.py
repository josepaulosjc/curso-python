print(True or False)

print( 7 != 3 and 2 > 3)

print( 'Operador AND ')
print( True and True)
print( True and False)
print( False and True)
print( False and False)

print( 'Operador OR ')
print( True or True)
print( True or False)
print( False or True)
print( False or False)

print( 'Operador XOR ')
print( True != True)
print( True != False)
print( False != True)
print( False != False)

print( 'Operador Unario ')
print(not True)
print(not False)
print(not 0) # Qualquer número diferente de 0 é verdadeiro
print(not 1)

# Cuidado com Operadores Bit a Bit
print( 3 & 2) # AND
print( 4 | 5) # OR
print( 2 ^ 4) # XOR


# Desafio Operadores Lógicos
trabalho_terca = True
trabalho_quinta = False

'''
-- Confirmando os 2: TV 50' + Sorvete
-- Confirmando apenas 1: TV 32' + Sorvete
-- Nunhum Confirmado: Fique em casa
'''

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta       # XOR
saude = not sorvete

print('TV 50 = {}, TV 32 = {}, Sorvete = {}, Saude = {}'.format(tv_50, tv_32, sorvete, saude))
