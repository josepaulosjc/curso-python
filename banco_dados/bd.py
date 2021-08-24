from mysql.connector import connect
from contextlib import contextmanager
# Decorator que criará conexao com o BD

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='159753',
    database='agenda'
)


@contextmanager     # Decoração do Generator
def nova_conexao():
    conexao = connect(**parametros) # Cria uma conexão com base nos parametros
    try:
        yield conexao 
    finally:
        if (conexao and conexao.is_connected()):    # Fecha a conexão ao terminar o bloco
            conexao.close()
