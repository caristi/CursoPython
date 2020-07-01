from User import User
from UserDao import UserDao as userDao

opcion = None

while opcion != 5:
      print("Opciones")
      print("1. Listar usuarios")
      print("2. Agregar usuario")
      print("3. Actualizar usuario")
      print("4. Eliminar usuario")
      print("5. Salir")
      
      opcion = int(input("Digite la opcion que desea: "))
      if opcion == 1:
         users = userDao.to_select()  
         for u in users:
            print(u)
            
      elif opcion == 2:
          username = input('Ingrese el username: ')
          password = input('Ingrese el password: ')
          
          user = User(username=username,password=password)          
          userDao.to_insert(user)
          
      elif opcion == 3:
          username = input('Ingrese el username: ')
          password = input('Ingrese el password: ')
          id = int(input("Id para actualizar "))
                    
          user = User(id=id,username=username,password=password)          
          userDao.to_update(user)
      elif opcion == 4:
          id = int(input("Id para eliminar: "))
          user = User(id=id)
          userDao.to_delete(user)
else:
  print("Salimos del progarma")