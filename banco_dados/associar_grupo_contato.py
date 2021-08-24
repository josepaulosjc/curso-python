from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s '

contato_grupo = {
    'Ana': 'Casa',
    'Bia': 'Trabalho',
    'Luca': 'Casa',
    'Lu': 'Casa',
    'Gui': 'Trabalho',
    'Beca': 'Casa',
    'Pedro': 'Trabalho',
    'João': 'Trabalho'
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            # Executa a Primeira Query passando o grupo e pegando o id
            cursor.execute(selecionar_grupo, (grupo,))
            # Pega o id do grupo com fetchone no indice 0
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato,(grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('contatos associados')

