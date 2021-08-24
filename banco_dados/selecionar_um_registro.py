from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT tel, nome FROM contatos LIMIT %s OFFSET %s'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql, (10,10))

    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
