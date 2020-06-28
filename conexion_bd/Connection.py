import sys
from Logger import logger
from psycopg2 import pool


class Connection:
    __DATEBASE = 'testdb'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'

    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def get_pool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CON, 
                                                       cls.__MAX_CON,
                                                       user=cls.__USERNAME,
                                                       password=cls.__PASSWORD,
                                                       host=cls.__HOST,
                                                       port=cls.__DB_PORT,
                                                       database=cls.__DATEBASE)
                return cls.__pool
            except Exception as e:
               logger.error(f'Erro conexion BD {e}')
               sys.exit()
        else:
           return cls.__pool           

    @classmethod
    def get_connection(cls):          
        connection = cls.get_pool().getconn() 
        return connection

    @classmethod
    def break_free_connection(cls,conn):
        cls.get_pool().putconn(conn)    
          
    @classmethod
    def close_connection(cls):
        cls.get_pool().closeall()
  
if __name__ == '__main__':
  connection1 = Connection.get_connection()