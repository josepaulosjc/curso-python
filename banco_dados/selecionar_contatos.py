from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (10,10))
        contatos = cursor.fetchall()
    except ProgramingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} Telefone: {contato[1]}') #:2d se refere a dois digitos

