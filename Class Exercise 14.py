from dataclasses import dataclass

@dataclass
class Customer:
    
    id:str
    firstName:str 
    lastName:str 
    company:str 
    address:str
    city:str 
    state:str 
    zipcode:str
    

    def fullName(self):
       
        return self.firstName + self.lastName
    
    def fullAddress(self):
        
        return (self.address + self.city + self.state + self.zipcode)
