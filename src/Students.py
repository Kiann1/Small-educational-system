"""
    Here we have a student class that inherits from the Person class we defined previously. 
    It inherits all the properties of its parent. Using the super method, 
    you can access the parent class's properties within the child class. 
    Next, we defined a method called "add_courses" (which represents behaviors). 
    The input of this method is a list of course names. 
    Then, using a loop, we assign the elements of the list (which are the course names) 
    to the key variable. Next, we check whether the names of these courses 
    exist in the dictionary or not (this dictionary contains student information 
    such as name, last name, student ID, and courses; it's a nested dictionary). 
    Then we set the course names as keys in the internal dictionary and assign 
    an empty value to them because grades will be applied by the instructor.
    
    ----
    To view all the module description, you can refer to the README file.
    (-_-)
"""

from src.Person import Person

class Students(Person):
    
    def __init__(self, name : str , last_name : str, 
                 std_code : int):
        
        super().__init__(name, last_name)
        
        self.std = std_code 
        self.courses = {}
        
    def add_course(self, course_name : list):
        
        for key in course_name:
            
            if key not in self.courses:
        
                self.courses[course_name] = None
        
            
        
        
        
        
        
        
        