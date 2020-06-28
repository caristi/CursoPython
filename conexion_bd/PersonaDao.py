from loggin import logger
from Connection import Connection


class PersonDao:

    __SELECT = 'SELECT * FROM persona'
    __INSERT = 'INSERT INTO persona(nombre,apellido,email) values(%s,%s,%s)'
    __UPDATE = 'UPDATE persona set nombre = %s where id = %s'
    __DELETE = 'DELETE FROM persona WHERE id = %s'

    def __init__(self):
        super().__init__()

    @classmethod
    def to_select(cls):
        logger.info('Inicia Select')
        try:
            cursor = Connection.get_cursor()
            cursor.execute(cls.__SELECT)
            registros = cursor.fetchall()

            for person in registros:
                print(person)

            return 0
        except Exception as e:
            logger.error(f'Error a la hora de realizar la consulta: {e}')   
        finally:
            Connection.close()
            
        logger.info('Termina Select')

    @classmethod
    def to_insert(cls, person):
        logger.info('Inicia Insert')
        try:
            connection = Connection.get_connection()
            cursor = Connection.get_cursor()

            valores = (person.get__name(), person.get__last_name(),
                       person.get__email())
            cursor.execute(cls.__INSERT, valores)
            connection.commit()
            
            return 0

        except Exception as e:
            logger.error(f'Error a la hora de realizar la insertar: {e}')
        finally:
            Connection.close()
        
        logger.info('Termina Insert')

    @classmethod
    def to_update(cls, person):
        try:
            connection = Connection.get_connection()
            cursor = Connection.get_cursor()

            valores = (person.get__name(), person.get__id_person())
            cursor.execute(cls.__UPDATE, valores)
            connection.commit()

        except Exception as e:
            logger.error(f'Error a la hora de realizar la update: {e}')
        finally:
            Connection.close()

    @classmethod
    def to_delete(cls, id_person):
        try:
            connection = Connection.get_connection()
            cursor = Connection.get_cursor()

            valores = (id_person,)
            cursor.execute(cls.__DELETE, valores)
            connection.commit()

        except Exception as e:
             logger.error(f'Error a la hora de realizar la delete: {e}')
        finally:
            Connection.close()
