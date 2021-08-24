'''
TDD - Test driven development (Desenvolvimento dirigido por Testes)

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o codigo e ver o teste passar

Refactor
Parte 3 -> Melhorar meu codigo
'''

import unittest
from baconcomovos import bacon_com_ovos

class TestBaconComOvos(unittest.TestCase):
    # Esse Teste deve levantar uma exceção no tipo da variavel, não aceitando qualquer valor diferente de int
    def test_bacon_com_ovos_deve_levantar_assrtion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos(' ')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_multiplo_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        # O Retorno de 'entrada' deve ser igual a 'saida'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" nao retornou "{saida}"'
                )
    
    def test_bacon_com_ovos_deve_retornar_passar_fome_se_nao_multiplo_3_nem_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        # O Retorno de 'entrada' deve ser igual a 'saida'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" nao retornou "{saida}"'
                )
    
    def test_bacon_com_ovos_deve_retornar_bacon_se_multiplo_somente_de_3(self):
        entradas = (3, 6, 9, 12, 21)
        saida = 'Bacon'

        # O Retorno de 'entrada' deve ser igual a 'saida'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" nao retornou "{saida}"'
                )
    
    def test_bacon_com_ovos_deve_retornar_bacon_se_multiplo_somente_de_5(self):
        entradas = (5, 20, 25, 40, 50)
        saida = 'Ovos'

        # O Retorno de 'entrada' deve ser igual a 'saida'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" nao retornou "{saida}"'
                )

unittest.main(verbosity=2)