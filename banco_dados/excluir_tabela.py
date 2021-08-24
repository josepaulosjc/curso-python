from bd import nova_conexao
from mysql.connector import ProgrammingError


exclui_tabela = '''
DROP TABLE IF EXISTS emails
'''
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(exclui_tabela)
        except ProgrammingError as e:
            print(f'Erro ao excluir, {e.msg}')
except:
    print(f'Erro CONEXÃO: {e.msg}')