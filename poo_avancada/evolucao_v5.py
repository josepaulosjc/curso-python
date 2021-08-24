# --------- Classes Abstratas (Anonima) --------- #

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None  # Atributo Privado

    @property
    def inteligente(self):
        raise NotImplementedError('Propriedade nao implementado')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
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

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    anonimo = Humano('John Doe')

    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('Propriedade abstrata')

    jose = HomoSapiens('Jose')
    print('{} da classe {}, inteligente: {}'.format(
        jose.nome, jose.__class__.__name__, jose.inteligente))

    grokn = Neanderthal('Grokn')
    print('{} da classe {}, inteligente: {}'.format(
        grokn.nome, grokn.__class__.__name__, grokn.inteligente))
