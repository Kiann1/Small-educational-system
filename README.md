# Small-educational-system

1-  Person :

     First, we have a person class that has two attributes, 
    one of which is name and the other is last name.

2- Students :

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

3- Prof :

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
    
4- student_profile :

    In this section, we have a function called "enter_student_details," 
    which takes the inputs of the student's first name, last name, student ID, 
    and the courses the student has taken. Inside this function, 
    there is a dictionary that stores this information. 
    The value corresponding to the "courses" key in this dictionary is another dictionary. 
    In fact, we created a nested dictionary where the course names serve as keys, 
    and the grades are stored as values (by default, the grades for courses are set to None). 
    Finally, we return this dictionary.
    
5- save_to_json_file :

    Here we first import the json module. 
    Then, we define a function called "save_to_json." 
    The inputs of this function are our JSON file and a dictionary 
    containing student information. Next, we use the open function 
    to open the JSON file and utilize the write mode. 
    After that, using the dump function, we save the dictionary into the JSON file.

6- extract_the_json_file :

    Here we intend to extract the JSON file. First, we import the json module. 
   Then, we create a function called "extract_json_file," 
   which takes a JSON file as input. Next, we use the open function with the read mode. 
   After that, we define a variable to assign the extracted file, 
   which is a dictionary, 
   to the variable "std_information" (we can extract the JSON file using the load function). 
   Finally, we return the variable "std_information."

7- pass_or_fail :

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


8- calculate_the_average :

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
    



9 - main :

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


                                "Farewell (-_+)"