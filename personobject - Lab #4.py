#LAKSHMI URJITHA DHADIGAM - LAB 4-1223270

from dataclasses import dataclass
@dataclass
class Person:
    firstname:str=""
    lastname:str=""
    email:str=""

    @property
    def fullname(self):
        return self.firstname + self.lastname
    
@dataclass
class Customer(Person):
    number:str=""
    
@dataclass    
class Employee(Person):
    ssn:str=""

    
    
