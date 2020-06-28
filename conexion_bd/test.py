from PersonaDao import PersonDao
from Person import Person

personDao = PersonDao()

person = Person(None,'Carlos','García Aristizábal','cgarcia@gmail.com')
personDao.to_insert(person);

person1 = Person(22,'Carlos',None,None)
personDao.to_update(person1)

personDao.to_delete(25)

personDao.to_select()
