"""
   Here we intend to extract the JSON file. First, we import the json module. 
   Then, we create a function called "extract_json_file," 
   which takes a JSON file as input. Next, we use the open function with the read mode. 
   After that, we define a variable to assign the extracted file, 
   which is a dictionary, 
   to the variable "std_information" (we can extract the JSON file using the load function). 
   Finally, we return the variable "std_information."
"""

import json

def extract_json_file (information):
    
    with open(information , 'r') as jf:
        
       std_information = json.load(jf)
    
    return std_information