from locale import setlocale, LC_ALL  # Importa a Linguagem
from calendar import mdays, month_name  # quantidades de dias, e nome de meses
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')
# print(month_name[1])
# print(mdays[1])


# Listar todos os meses com 31 dias
# 1. (filter) Pegar todos os Indíces dos meses com 31
# 2. (map) Transformar índices em nomes
# 3. (reduce) Juntar tudo para imprimir

meses_31 = list(filter(lambda mes: mdays[mes] == 31, range(1, 13)))

meses_nomes = list(map(lambda mes: month_name[mes], meses_31))

juntar_meses = reduce(
    lambda todos, nome_mes: f'{todos}\n- {nome_mes}', meses_nomes, 'Meses com 31 dias: ')

# print(meses_31)
# print(meses_nomes)
print(juntar_meses)
