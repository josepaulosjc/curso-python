# O ponto diz que estamos importando de forma relativa, ou seja na mesma pasta
from .pessoa import Pessoa


def get_data(compra):
    return compra.data


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        # Retorna Null se não tiver nada na lista de compras
        # Se tiver ordena as compras e pega o ultimo item por data
        return None if not self.compras else \
            sorted(self.compras, key=get_data)[-1].data

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total
