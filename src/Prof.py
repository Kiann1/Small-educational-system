"""
    Here we have a Professor class that inherits from the Person class, 
    similar to the Student class. Again, we use the super method as we discussed 
    before to inherit properties from the parent class. We designed a method for 
    the Professor class to enter grades for courses. 
    The inputs of this method are a dictionary 
    (the same dictionary containing student information and their selected courses) 
    and a list of courses, and finally, a list of grades entered by the professor. 
    So, this method has three inputs.

    In this method, first, using a loop and 
    the zip function (which takes multiple iterables like lists, dictionaries, 
    and strings as input arguments and returns an iterator that aggregates elements 
    from each of the iterables), 
    we assign grades and courses to the input argument of the zip function, 
    which then assigns them to two variables named "course" and "grade". 
    Then, we assign the grades to the desired courses that exist within our 
    nested dictionary as values, and after finishing the loop, we return this dictionary.
    
    ----
    To view all the module description, you can refer to the README file.
    (-_-)
"""

from src.Person import Person
class prof (Person):
    
    def __init__(self, name: str, last_name: str , prof_code : int):
        super().__init__(name, last_name)
        
        self.prof_code = prof_code
    
    def enter_grades (self, dict_information : dict , courses : list , grades : list):
        
        for course , grade in zip(courses, grades):
            
            
                dict_information["courses"][course] = grade
        
        
        return dict_information
        
        
        
        
            
            
                    
                    
    
            
            
        
        