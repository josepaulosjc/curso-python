from locale import setlocale, LC_ALL  # Importa a Linguagem
from calendar import mdays, month_name  # quantidades de dias, e nome de meses
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses com 31 dias
# 1. (filter) Pegar todos os Indíces dos meses com 31
# 2. (map) Transformar índices em nomes
# 3. (reduce) Juntar tudo para imprimir


def mes_com_31_dias(mes): return mdays[mes] == 31


def get_nome_mes(mes): return month_name[mes]


def juntar_meses(todos, nome_mes): return f'{todos}\n- {nome_mes}'


print(
    reduce(juntar_meses,
           # Filter faz um range de 1 a 12, e retorna os meses com mais de 31 dias
           # Map pega essa lista e itera cada um dos itens devolvendo uma nova lista apenas com os nomes
           # Por fim o Reduce cria um acumulador 'todos' e itera entre os meses concatenando a string ao acumulador
           map(get_nome_mes, filter(mes_com_31_dias, range(1, 13))),
           'Meses com 31 dias:'
           )
)
