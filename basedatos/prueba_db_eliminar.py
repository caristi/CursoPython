import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='testdb')

cursor = conexion.cursor()
sql = 'DELETE FROM persona WHERE id = %s'
valores = (7,)
cursor.execute(sql,valores)
conexion.commit()
registros = cursor.rowcount
print(registros)