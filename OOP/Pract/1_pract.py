class Person:
    a = 10
    name: str # - игнорируется классом, просто для читаемости
    #def __new__(cls, *args, **kwargs):
    #    return super().__new_(cls) # -  super() - обращение к родителю класса

    def __init__(self, name):
        #self.name = name #intance attribute public
        #self._name = name # protected
        self.name = name # public

    def print(self):
        print(self.__name)

    # region properties

    #getter
    def get_name(self):
            return self.__name
    
    #setter
    def _set_name(self, name):
         if len(name) > 128:
              raise ValueError('daun')
         self.__name = name

    # property getter
    @property
    def name(self):
         return self.__name
    
    # property setter
    @name.setter
    def name(self, name):
         if len(name) > 128:
              raise ValueError('daun')
         self.__name = name

    # endregion
    @staticmethod
    

    @classmethod
    def cals_age_cls(cls, date_of_birth): # cls подставляется сам
         ...
    
def calc_age(date_of_birth):
    ...
    # нет смысла писать static методы внутри класса

    
person = Person('Semenov') # __new__ -> __init__ - передается в self = *this c++
'''print(type(person))
print(person.name)

person1 = Person('Ishanov')
print(person1.name)
print(person1._name)
print(person1.__dict__)
print(person1._Person__name)
person1.__name = 'Oleja' # != __name из класса 
print(person1.__dict__)
print(person.__dict__)
person1.print()
person1.print = lambda: print('ihihih')
person1.print()
# питон легко тестируется unit тестами, в отличие от других языков'''


print(person.name)
person.name = 'Kitty'
print(person.name)
print(Person.a)
print(person.a)
person1 = Person('doggy')
print(person1.a) # обращение к статической
person1.a = 11 # != "а" из класса, обращение к динамической, лучше обращаться Person.a
print(person.a)
print(person1.a)


class Poind2d:
     def __init__(self, x, y):
          self.x, self.y = x, y
class Vector2d:
    def __init__(self, x, y):
          self.x, self.y = x, y

    @classmethod
    def from_points(cls, self, start, end):
         return cls(end.x - start.x, end.y - start.y)

    # два инита не будут работать

v1 = Vector2d(x = 10, y = 20)
v2 = Vector2d.from_points(
     start = Poind2d(x=10, y=10),
     end = Poind2d(x = 34, y = 34)
)






