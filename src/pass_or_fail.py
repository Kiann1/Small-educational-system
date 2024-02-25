"""
    In this section, we want to determine which courses the student has passed 
    and which ones they have failed.
    
    First, we import the json module. Then, we define a function called "pass_or_fail," 
    which takes a JSON file containing student information as input. 
    Next, we use the open function to open the file with the read mode.
    
    We define a variable named "std_inf" and assign the extracted file to it.
    
    Next, we define two variables, "passed_courses" and "failed_courses," 
    with empty dictionaries inside them.

    Using a loop and the items() function of the internal nested dictionary 
    (which contains the course names the student has taken and their grades),
    we assign the items to variables "course" and "grade." Inside the loop, 
    we have a condition that checks if the grade of the respective 
    course is greater than 10 or not. If it is greater than 10, 
    it assigns the course name as a key and the grade as a value to 
    the dictionary "passed_courses." Otherwise, if the grade is less 
    than 10 and greater than zero, it assigns the course
    name as a key and the grade as a value to the dictionary "failed_courses."
    
    To display the passed and failed courses:
- First, we print a message displaying the passed courses.
- Then, we use a loop to iterate through the items (key-value pairs) 
of the dictionary "passed_courses" using the items() function, 
assigning the items to variables "course" and "grade." Then, using the print 
statement and f-string, we display the courses and their grades to the user.

- Similarly, for displaying the failed courses, we use the same method.
"""

import json

def pass_or_fail (information_file):
    
    with open(information_file , 'r') as jf :
        
        std_inf = json.load(jf)
    
    passed_courses = {}
    failed_courses = {}
     
    for course , grade in std_inf["courses"].items():
        
        if grade <= 20 and grade >= 10:
            
            passed_courses[course] = grade
            
        elif grade < 10 and grade >= 0:
            
            failed_courses[course] = grade
            
    print("Pass these courses : ")
    for course , grade in passed_courses.items():
        
        print(f"{course} : {grade}")
        
    print("\nFailed courses : ")
    for course , grade in failed_courses.items():
        
        print(f"{course} : {grade}")
            
        
        