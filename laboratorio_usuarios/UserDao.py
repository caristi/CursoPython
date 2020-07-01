from Logger import logging
from CursorPool import CursorPool
from User import User 

class UserDao:
    __SELECT = 'SELECT * FROM public.user'
    __INSERT = 'INSERT INTO public.user(username,password) VALUES(%s,%s)'
    __UPDATE = 'UPDATE public.user SET username = %s, password = %s WHERE id = %s'
    __DELETE = 'DELETE FROM public.user WHERE id = %s'

    @classmethod
    def to_select(cls):
        with CursorPool() as cursor:
            cursor.execute(cls.__SELECT)
            records = cursor.fetchall()
            users = []
            for row in records:
                user = User(row[2],row[0],row[1])
                users.append(user)
                
        return users
    
    @classmethod
    def to_update(cls,user):
        with CursorPool() as cursor:
            values = (user.get_username(), user.get_password(),user.get_id())
            cursor.execute(cls.__UPDATE,values)
            
    @classmethod
    def to_insert(cls,user):
        with CursorPool() as cursor:
            values = (user.get_username(),user.get_password())
            cursor.execute(cls.__INSERT,values)
    
    @classmethod
    def to_delete(cls,user):
        with CursorPool() as cursor:
            value = (user.get_id(),)
            cursor.execute(cls.__DELETE,value)