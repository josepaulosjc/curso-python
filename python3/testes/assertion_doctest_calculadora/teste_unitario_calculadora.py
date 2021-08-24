import unittest
from calculadora import soma

# Deve herdar classe TestCase do Modulo Unittest
# Toda função deve começar com 'test_'


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)
    
    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(5,-5), 0)
    
    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200)
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):     # Deve definir o Contexto SubTeste
                x, y, saida = x_y_saida                 # Faz o Unpaking das tuplas para cada variável
                self.assertEqual(soma(x,y), saida)
    
    def test_soma_x_nao_e_int_ou_float_deve_retornar_asserterror(self):
        with self.assertRaises(AssertionError):
            soma('11', 5)
    
    def test_soma_y_nao_e_int_ou_float_deve_retornar_asserterror(self):
        with self.assertRaises(AssertionError):
            soma(7, '5')
    
    


unittest.main(verbosity=2)
