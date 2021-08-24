# --------- Tipos de Metodos --------- #

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthaleasis'
        return self

# Metodos Estaticos
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthaleasis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

# Metodo de Classe
    @classmethod
    # Verifica se e a ultima especie retornada pela funcao especie
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    # HomoSapiens.das_cavernas(jose)
    grokn = Neanderthal('Gronk')
    print(
        f'Evolucao (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolucao (a partir da instacia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')
    print(f'Jose evoluido? {jose.is_evoluido()}')
    print(f'Gronk evoluido? {grokn.is_evoluido()}')
