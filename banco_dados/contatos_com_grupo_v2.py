from collections import defaultdict
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
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            # Como os contatos já forma armazenados em uma variavel
            # Podemos encerrar o 'cursor'
            cursor.close()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        # DefaultDict define uma lista com uma chave padrão, devolve uma lista
        agrupados = defaultdict(list) 
        for contato in contatos:
            # Define a chave sendo o 'Grupo'
            agrupados[contato["grupo"]].append(contato["nome"])
            
        print(agrupados)


