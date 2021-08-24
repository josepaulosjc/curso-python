class Data:
    # def to_str(self):  # 1a Forma
    def __str__(self):   # 2a Forma - Converte Objeto em String
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
# print(d1.to_str())    # 1a Forma
print(d1)               # 2a Forma

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
# print(d2.to_str())    # 1a Forma
print(d2)               # 2a Forma
