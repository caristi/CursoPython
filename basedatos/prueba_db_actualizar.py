import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='testdb')

cursor = conexion.cursor()
sql = 'UPDATE persona SET nombre = %s WHERE id = %s'
valores = ('HUGO',4)
cursor.execute(sql,valores)
conexion.commit()

valores = (('HUMBERTO',6),
           ('CARLOS HUGO',7))

cursor.executemany(sql,valores)
conexion.commit()

registros = cursor.rowcount
print(registros)
cursor.close()
conexion.close()