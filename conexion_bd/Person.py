class Person:
    
    def __init__(self,id_person,name,last_name,email):
        self.__id_person = id_person
        self.__name = name
        self.__last_nanme = last_name
        self.__email = email
        
    def get__id_person(self):
        return self.__id_person
    
    def get__name(self):
        return self.__name
    
    def get__last_name(self):
        return self.__last_nanme
    
    def get__email(self):
        return self.__email
    