class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._agetwice = age*2
        self.__agesquared = age**2
    
    def display(self):
        print(f"name: {self.name}, age: {self.age}")

    @staticmethod
    def info():
        print("This Class consists of Info about a person")

    def print_squared_age(self):
        print(f"Squared Age of a Person : {self.__agesquared}")

    @classmethod
    def get_date_of_birth(cls,date_string):
        day, month, year = map(int, date_string.split(','))
        return (day, month, year)

    def get_professional_info(self,company= None, Role=None,Experience = None, Programming = None):
        if company!= None: 
            print(f"Company : {company}",end= " ")
        
        if Role!= None: 
            print(f"Role : {Role}",end= " ")

        if Experience!= None: 
            print(f"Experience : {Experience}",end= " ")
        
        if Programming!= None: 
            print(f"Programming : {Programming}",end= " ")
        
        print()

s1 = A("Phani",24)
s1.display()
s1.info()
print(f"Double Age of a Person : {s1._agetwice}")
# print(f"Squared Age of a Person : {s1.__agesquared}") # we cannot use this outside from the class

s1.print_squared_age() # we can access that variable from here
print(s1.get_date_of_birth("06,09,2000"))

# Python doesnt allow method overloading, but we can achieve this by using keyword args
# below are the examples 
s1.get_professional_info(company="ThunderSoft")
s1.get_professional_info(Role="Developer")
s1.get_professional_info(company="ThunderSoft", Role="Developer", Experience="3Yrs")



# Abstract Methods

from abc import ABC,abstractmethod

class Person(ABC): # this is a abstract class, since it has abstract method
    @abstractmethod
    def person_name(self):
        pass  # this function can we redefined by the inherited class object


class PersonInfo(Person):

    def __init__(self,name):
        self.name = name
    
    def person_name(self):
        print(f"Name of the Person is : {self.name}")


c = PersonInfo("Phani")
c.person_name()