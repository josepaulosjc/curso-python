print( 2 + 3 )
print( '2' + '3' )
#print( 2 + '3' ) -> Não funciona

a = 2
b = '3'
print(type(a))
print(type(b))

print(a + int(b))
print(str(a) + b)

#print(a + int('3.4'))  -> Não Funciona
print(a + float('3.4')) 