soma = 1.1 + 2.2
print(soma) # Soma por bit que dará errado


from decimal import Decimal, getcontext
resultado = Decimal(1) / Decimal(7)

print(resultado)                        # 0.1428571428571428571428571429


getcontext().prec = 4                   # Define precisão de casas decimais para 4
resultado = Decimal(1) / Decimal(7)     # Executa Novamente

print(resultado)                        # 0.1429

maximo = Decimal.max(Decimal(1),Decimal(7))
print(maximo)

getcontext().prec = 12
soma = Decimal(1.1) + Decimal(2.2)
print(soma)

# O que está disponível em Decimal
print(dir(Decimal))

# O que está disponível no 'Módulo' decimal
import decimal
print(dir(decimal))

