"""
    First, we have a person class that has two attributes, 
    one of which is name and the other is last name.
    
    ----
    To view all the module description, you can refer to the README file.
    (-_-)

"""
class Person:
    
    def __init__ (self, name : str, last_name : str):
        
        self.name = name 
        self.family = last_name
        
    