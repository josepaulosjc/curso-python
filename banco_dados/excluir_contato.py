from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'DELETE FROM contatos where nome = %s'
args = ('Lucas',) # A virgula ',' faz o interpretador identificar como tupla

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s).')
    