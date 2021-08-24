import psycopg2

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"


print('Conectando ao Banco...')
try:
    con = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

except:
    raise


query = 'select * from account'

# ------ Navegando por Cursor ---------- #
cursor = con.cursor()                       # Realiza conexão
cursor.execute(query)                       # Executa Query


# Trazendo Cada resultado em elementos -- "FetcOne"
for registro in cursor:
    print('Usuario: {} email: {} data criacao:{}'.format(
        registro[0], registro[3], registro[4]))

con.close()
print('Conexao Encerrada!')
