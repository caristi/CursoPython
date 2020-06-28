from PersonaDao import PersonDao
from Person import Person

personDao = PersonDao()

personDao.to_select()

person = Person(None,'Carlos Hugo','Aristizábal García','carloshugo5@gmail.com')
personDao.to_insert(person);
"""
person1 = Person(22,'Carlos',None,None)
personDao.to_update(person1)

personDao.to_delete(25)

personDao.to_select()"""
