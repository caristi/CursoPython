import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='testdb')

cursor = conexion.cursor()
sql = "SELECT * FROM persona"
id_persona = ((1, 3))
llave = (id_persona,)
cursor.execute(sql, llave)
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conexion.close()
