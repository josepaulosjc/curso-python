'''
class Pessoa
    __init__
        nome str
        sobrenome str
        dados
        -obtidos bool
    API:
        obter_todos_os_dados -> method
            OK
            404

        ( dados_obtido será True se obtidos com sucesso)
'''

import unittest
from unittest.mock import patch
from Pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    # Metodos pré e pós teste, 
        # Antes: setUp() -> antes, setUpClass(cls)
        # Depois: tearDown() -> depois
    def setUp(self):
         self.p1 = Pessoa('Luiz', 'Otavio')
         self.p2 = Pessoa('Maria', 'Miranda')
    
    def test_pessoa_attr_nome_valor_coreto(self):
        self.assertEqual(self.p1.nome, 'Luiz')
        self.assertEqual(self.p2.nome, 'Maria')
    
    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)
    
    def test_pessoa_attr_sobrenome_valor_coreto(self):
        self.assertEqual(self.p1.sobrenome, 'Otavio')
        self.assertEqual(self.p2.sobrenome, 'Miranda')
    
    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dadosobtidos)
        self.assertFalse(self.p2.dadosobtidos)

    # Utilizar dados Fake para não comprometer o codigo com uma API Externa
    # Faz uma requisição fake e verifica se a resposta.ok é True (precisa ser o mesmo atributo)
    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True 
            self.assertEqual(self.p1.obter_todos_os_dados(),'CONECTADO')
            self.assertTrue(self.p1.dadosobtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(),'CONECTADO')
            self.assertTrue(self.p2.dadosobtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(),'ERRO 404')
            self.assertFalse(self.p1.dadosobtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(),'ERRO 404')
            self.assertFalse(self.p2.dadosobtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(),'CONECTADO')
            self.assertTrue(self.p1.dadosobtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(),'CONECTADO')
            self.assertTrue(self.p2.dadosobtidos)

            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(),'ERRO 404')
            self.assertFalse(self.p1.dadosobtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(),'ERRO 404')
            self.assertFalse(self.p2.dadosobtidos)  

if __name__ == '__main__':
    unittest.main(verbosity=2); # verbosity mostra todo o erro