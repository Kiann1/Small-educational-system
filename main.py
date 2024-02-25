"""
    "At the final stage, we want to use all the modules we've written. First, 
    we import all of them, 
    then we define a function named main.
    In the main function, we first define a variable named 'running' and assign True to it.
    Next, we use a while loop with the condition that the 'running' variable is True, 
    essentially creating an infinite loop.
    Then we call the menu function to display the menu.
    Next, we prompt the user to enter their choice and assign it to the 'choices' variable.
    
    1-Student panel:
    
    We then use a condition stating that if 'choices' is a string containing a 
    digit (using the isdigit() function) and it equals '1', the condition is met.
    Once inside the condition, we first call the student_page() function to display the student panel.
    Then we prompt the user again to enter their desired option.
    We convert the user input to lowercase using the lower() function.
    We use another condition to check if the user has selected an option, and if so, the following events occur:
    
    Options: "std", "grd", "pf", "avg", and "ext".


    Std:

    If the user enters 'std', we ask for their name, surname, student ID, 
    and the courses they want to choose, and they must enter them.
    Next, using the split() function, we separate the entered courses and store them in a list.
    Next, by calling the Student class with the name, surname, and student ID as inputs, 
    we assign them to the variable 'std_1', essentially creating an object of the Student class.
    We use another condition to impose a restriction on the number of selected courses for the student, 
    which should not exceed 6.
    We use the len function to count the number of courses.
    If the number of courses is less than or equal to 6, we enter the condition.
    Inside the condition, we use a loop to assign the list of courses to the 'course' 
    variable and pass them as arguments to the method we wrote to add a course inside the Student class.
    We then pass all the entered information and selected courses to the enter_student_details 
    function (previously described) and assign them to the 'dict_inf' variable.
    When we exit the loop, we call the save_to_json function and pass the JSON file 
    and 'dict_inf' as inputs to this function.
    If the condition for limiting the number of courses selected by the student becomes False, a message is displayed.
    
    Grd:

    If the user selects 'grd', we enter a condition where the JSON file is read 
    using the open function with 'r' mode, and it is extracted using the load function, 
    finally assigned to the 'dict_courses' variable, and printed.
    
    Pf:
    
    If the user selects 'pf', the pass_or_fail function is called, 
    and the JSON file is passed as input to it.
    
    Avg:

    If the user enters 'avg', the avg function is called, 
    and the JSON file is passed as input to the function.
    
    Ext:

    If the user enters 'ext', the message 'bye' is displayed, and the 'running' variable, 
    which was True, is set to False, exiting the loop.


    2-Professor panel:

    If the user enters '2', the professor_page() function is called, displaying the professor panel.
    Then we prompt for the professor's input, and they must choose one of these options, 
    with the user input converted to lowercase using the lower() function.
    
    Options: 'prfinf' and 'ext'.
    
    Prfinf:

    If the user selects 'prfinf', the professor must enter their name, surname, and code.
    Next, an object of the Professor class is created.
    Next, the extract_json_file function is used, taking the JSON file as input, 
    and it is assigned to the 'dict_std_inf' variable, which contains student information.
    Using the keys() function, we access the courses taken by the student 
    in a nested dictionary and convert them to a list, assigning them to the 'courses_list' variable.
    The list of courses is displayed using the print function and f-string.
    Next, an empty list named 'grades' is defined.
    We use a loop and assign the list of courses to the 'course_s' variable.
    Next, the courses are presented to the professor one by one, and the professor must enter the grades, 
    which are added to the 'grades' list using the append method.
    After the loop is completed, the enter_grades method, which we designed in the Professor class, 
    is called, passing the student's information, list of courses, and list of grades as inputs, 
    and assigning them to the 'grades_entered_by_the_professor' variable.
    Then it is saved to a JSON file using the save_to_json function.
    
    Ext:

    To exit the professor panel, the user must enter 'ext'. 
    A suitable message is displayed, and the 'running' variable is changed to False to exit the loop.
    If an irrelevant input is entered in the professor panel, a suitable message is displayed.
    
    
    3- To exit the program, the user can enter '3'.

    Finally, we call the main function."

    ----
    To view all the module description, you can refer to the README file.
    (-_-)
"""

import json
from src.Prof import prof
from src.Students import Students
from src.menu import menu
from src.calculate_the_average import avg
from src.pass_or_fail import pass_or_fail
from src.student_dashboard import student_page
from src.save_to_json_file import save_to_json
from src.professor_dashboard import professor_page
from src.student_profile import enter_student_details
from src.extract_the_json_file import extract_json_file

def main ():
    
    running = True
    
    while running:
        
        menu()
    
        choices = input("Select the desired option : ")
    
        if choices.isdigit() and choices == "1":
                
                student_page()
                
                choice_of_std_user = input("Select the desired option : ")
                choice_of_std_user = choice_of_std_user.lower()
                
                if choice_of_std_user == "std":
                            
                        name = input("Please enter your name : ") 
                        last_name = input("Please enter your last name : ")
                        std_code = int(input("Please enter your student code : "))
                        courses = input("Enter the courses you want to take comma-separated) maximum of 6 lessons:")
                            
                        courses = courses.split(",")                                        
    
                        std_1 = Students(name , last_name , std_code)

                        if len(courses) <= 6:
                                
                            for course in courses:
                    
                                std_1.add_course(course)
                                dict_inf = enter_student_details(name , last_name , std_code , std_1.courses)
                    
                            save_to_json("student_profile.json" , dict_inf)

                        else:
                            
                            print("\nElective course are more than allowed please try again")
                                
                                
                elif choice_of_std_user == "grd":
                            
                        with open("student_profile.json" , 'r') as jf_file:
                                
                            dict_courses = json.load(jf_file)
                            
                        print(dict_courses)
                            
                elif choice_of_std_user == "pf":
                    
                    pass_or_fail("student_profile.json")
                
                elif choice_of_std_user == "avg":
                    
                    avg("student_profile.json")
                        
                elif choice_of_std_user == "ext":
                        
                        print("Bye")
                        running = False
                else:
                    
                    print("The input id incorrect , please follow the instructions -_")
        
        
        elif choices.isdigit() and choices == "2":
            
                professor_page()
            
                choice_of_professor_user = input("Select the desired option : ")
                choice_of_professor_user = choice_of_professor_user.lower()
                
                if choice_of_professor_user == "prfinf":
                    
                    prof_name = input("Please enter your name : ")
                    prof_last_name = input("please enter your last name : ")
                    prof_code = int(input("please enter your prf_code : "))

                    prof_1 = prof(prof_name , prof_last_name , prof_code)
                    dict_std_inf = extract_json_file("student_profile.json")
                    
                    courses_lsit = list(dict_std_inf["courses"].keys())  
                    
                    print(f"List of lessons taken by the student : {courses_lsit} enter grades in order of courses ->")
                    
                    grades = []
                    
                    for course_s in courses_lsit:
                        
                        grade = float(input(f"Enter grade for {course_s} : "))
                        grades.append(grade)
                        
                    grades_entered_by_the_professor  = prof_1.enter_grades(dict_std_inf , courses_lsit , grades)                    
                    
                    save_to_json("student_profile.json" , grades_entered_by_the_professor)
                
                elif choice_of_professor_user == "ext":
                    
                    print("bye professor  (+_+)")
                    running = False
                
                else:
                    
                    print("The input id incorrect , please follow the instructions -_")
                        
        elif choices.isdigit() and choices == "3":
            
            print("bye" , "('-')")
            running = False
                    
if __name__ == "__main__":
    
    print(main())