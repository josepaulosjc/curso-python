#! python
# ----------- Exercício: Módulos ----------- #

from math import pi

raio = input('Informe o raio: ')
area_cricunferencia = pi * float(raio) ** 2
print('Área do círculo', area_cricunferencia)

print('Nome do módulo', __name__)
