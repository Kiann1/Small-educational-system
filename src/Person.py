"""
    First, we have a person class that has two attributes, 
    one of which is name and the other is last name.

"""
class Person:
    
    def __init__ (self, name : str, last_name : str):
        
        self.name = name 
        self.family = last_name
        
    