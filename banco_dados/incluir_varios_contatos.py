from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana',   '96765-4321'),
    ('Bia',   '97765-4321'),
    ('Luca',  '89765-4321'),
    ('Lu',    '8865-4321'),
    ('Gui',   '87765-4321'),
    ('Beca',  '81765-4321'),
    ('Pedro', '82765-4321'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    # Caso concluido, ele retornará o resultado do ultimo ID
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')