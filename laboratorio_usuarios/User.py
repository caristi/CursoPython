class User:     
 def __init__(self,id=None,username=None,password=None):
      self.__id = id
      self.__username = username
      self.__password = password
      
 def __str__(self):
      return 'Id: ' + str(self.__id) + ' username:' + self.__username 
     
 
 def get_id(self):
  return self.__id

 def set_id(self,id):
   self.__id = id
   
 def get_username(self):
   return self.__username

 def set_username(self,username):
   self.__username = username
   
 def set_password(self,password):
    self.__password = password
    
 def get_password(self):
     return self.__password