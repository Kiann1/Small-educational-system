"""
    Here we first import the json module. 
    Then, we define a function called "save_to_json." 
    The inputs of this function are our JSON file and a dictionary 
    containing student information. Next, we use the open function 
    to open the JSON file and utilize the write mode. 
    After that, using the dump function, we save the dictionary into the JSON file.
"""

import json

def save_to_json (information , dict_inf):
    
    with open (information , 'w') as file_js:
        
        json.dump(dict_inf , file_js , indent=4)
    
    