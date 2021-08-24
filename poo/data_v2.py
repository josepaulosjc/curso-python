class Data:
    def __init__(self, dia=1, mes=1, ano=1970):  # Método Construtor
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
print(d1)

d2 = Data(7, 11, 2020)
print(d2)

d3 = Data(ano=2021)
d3.dia = 3
d3.mes = 8
print(d3)
