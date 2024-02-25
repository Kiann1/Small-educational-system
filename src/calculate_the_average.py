"""
    In this section, we want to calculate the average grades of the student. 
    First, we import the json module. Then, we define a function called "avg," 
    which takes a JSON file containing student information as input. 
    In this function, we first extract the JSON file using the open 
    function with the read mode, and we store it in the variable "std_inf." 
    Here, we could also use the "extract_the_json_file" module. 
    
    Next, we calculate the length of the grades using the len function and assign it 
    to the variable "length." Then, using the sum function, 
    we sum up the student's grades and divide it by the "length." 
    We assign this value to the variable "avg_grade" and finally print it. 
    This function calculates the average grades of the student and can be used accordingly.
    
    ----
    To view all the module description, you can refer to the README file.
    (-_-)
"""

import json

def avg (information):
    
    with open(information , 'r') as jf:
        
        std_inf = json.load(jf)
        
    length = len(std_inf["courses"].values())
    avg_grade = sum(std_inf["courses"].values()) / length
    
    print(f"Average grade : {avg_grade}")
    