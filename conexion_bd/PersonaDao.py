from Logger import logger
from CursorPool import CursorPool


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
        with CursorPool() as cursor:
            cursor.execute(cls.__SELECT)
            registros = cursor.fetchall()

            for person in registros:
                print(person)

    @classmethod
    def to_insert(cls, person):
        logger.info('Inicia Insert')
        with CursorPool() as cursor:
            valores = (person.get__name(), person.get__last_name(),
                       person.get__email())
            cursor.execute(cls.__INSERT, valores)

    @classmethod
    def to_update(cls, person):
        with CursorPool() as cursor:
         valores = (person.get__name(), person.get__id_person())
         cursor.execute(cls.__UPDATE, valores)


    @classmethod
    def to_delete(cls, id_person):
        with CursorPool() as cursor:
            valores = (id_person,)
            cursor.execute(cls.__DELETE, valores)
