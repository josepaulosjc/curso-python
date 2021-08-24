from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = '''
    SELECT 
        grupos.descricao AS grupo,
        contatos.nome AS nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, nome
'''

with nova_conexao() as conexao:
    try:
        # Com o cursor setado como dicionário, a resposta será um dicionário e não tuplas
        cursor = conexao.cursor(dictionary=True) # Não compatível com todos os bancos
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["nome"]}')


