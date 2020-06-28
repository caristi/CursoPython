import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='testdb')

cursor = conexion.cursor()
sql = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
valores = ('CARLOS H','CANO','CCANO@MAIL.COM')
cursor.execute(sql,valores)
conexion.commit()

valores = (('CARLOS HUMBERTO','CANO','CCANO@MAIL.COM'),
           ('CARLOS HUGO','CANO','CCANO@MAIL.COM'),
           ('CARLOS MARIO','CANO','CCANO@MAIL.COM'))

cursor.executemany(sql,valores)
conexion.commit()

registros = cursor.rowcount
print(registros)
cursor.close()
conexion.close()