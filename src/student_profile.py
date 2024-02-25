"""
    In this section, we have a function called "enter_student_details," 
    which takes the inputs of the student's first name, last name, student ID, 
    and the courses the student has taken. Inside this function, 
    there is a dictionary that stores this information. 
    The value corresponding to the "courses" key in this dictionary is another dictionary. 
    In fact, we created a nested dictionary where the course names serve as keys, 
    and the grades are stored as values (by default, the grades for courses are set to None). 
    Finally, we return this dictionary.
    
    ----
    To view all the module description, you can refer to the README file.
    (-_-)
"""

def enter_student_details (name_std , last_name_std , std_code , courses):
    
    student_profile = {"name" : name_std,
                       "family":last_name_std,
                       "student code":std_code,
                       "courses": courses
                      }
    
    
    return student_profile
    
        
        

