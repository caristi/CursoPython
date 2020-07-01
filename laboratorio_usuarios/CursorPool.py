from Connection import Connection
from Logger import logger

class CursorPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
        
    def __enter__(self):
        self.__conn = Connection.get_connection()
        self.__cursor = self.__conn.cursor()
        logger.info('Inicio connection')
        return self.__cursor
        
    def __exit__(self,exception_type,exception_value,exception_traceback):
        logger.info('Excuter funtion __exit__')
        
        if exception_value:
            self.__conn.rollback()
            logger.error(f'Error exception {exception_value}')
        else:             
            self.__conn.commit()
            
        self.__cursor.close()
        Connection.break_free_connection(self.__conn)
