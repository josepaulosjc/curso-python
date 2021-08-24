# --------- Propriedades --------- #

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None  # Atributo Privado

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

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
    jose.set_idade(40)
    print(f'Nome: {jose.nome}, Idade: {jose.get_idade()}')
