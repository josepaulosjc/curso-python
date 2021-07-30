print(dir(int))
print(dir(float))

a = 5
b = 2.5
c = a + b   # Resultado Float

print(type(a))
print(type(b))
print(type(c))

print(b.is_integer())
print(2.5.is_integer())
print(2.0.is_integer())

print((-2).__abs__())
print(abs(-2))