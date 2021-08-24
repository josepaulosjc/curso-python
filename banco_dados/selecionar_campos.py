from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT tel, nome FROM contatos LIMIT %s OFFSET %s'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql, (10,10))


    for contato in cursor.fetchall():
        # Percorre contatos, pega o campo, converte para srt e faz join com \t (LIST COMPREHENSION)
        print('\t'.join(str(campo) for campo in contato))
