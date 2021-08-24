from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Lucas', '98765-4321')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    # Caso concluido, ele retornará o resultado do ultimo ID
    else:
        print('1 registro incluido, ID:', cursor.lastrowid)