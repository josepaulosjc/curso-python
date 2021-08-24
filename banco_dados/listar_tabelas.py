from bd import nova_conexao
from mysql.connector import ProgrammingError

listar_tabelas = 'SHOW TABLES'

try:
    with nova_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(listar_tabelas)

        for i, tabela in enumerate(cursor, start=1):
            print(f'Tabela {i}: {tabela}')
            
except ProgrammingError as e:
    print(f'Erro ao listar tabelas, {e.msg}')
