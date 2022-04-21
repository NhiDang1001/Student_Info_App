# Student_Info_App

- Link to code: [here](https://github.com/NhiDang1001/Student_Info_App/blob/main/StudentInfoApp.py)

User enters a student name, score, 1/0 for graded or pass/fail basis.

Compute and display average score, input_count, average_graded_score, number of As,

Bs, 100s, 0s.

Input: name(str), score(float), graded(int)

Output: submit shows name, score, status, grade. summary shows average score,

average graded score, number of inputs, count of As, Bs, 100s, 0s.

### Functions
`submit()` 

Read name,score (integer),graded or passfail (1/0), upper or lower division(1/0) from the user. Validate each input other than name, using individual bool functions, and infinite loops. For example, if the entry for upper/lower was 2, you report an error, and prompt the user to enter that input again, and keep repeating that till the 1/0 input is validated.  

Add a method to the student class that will allow you to use the print() function in submit to display the attributes of the student object. 

Add the student object to the list.

`display()`

Loops through the list of students, and displays each student. 
Add a new method to the class to return a formatted string for use by display function. 

`save()`  

Opens a file for writing, loops through the students list, and writes info for each student to the file.

Save checks if data needs to be saved before saving to the file. All the data may have been saved already. 

Save() prompts the user to enter a filename to save to. However, this happens only the first time; subsequent saves will use the filename provided by the user at first save. We assume the file is to be saved to the same folder; the user need not be given the option to specify a file location.

`load()` 

To read a text file that contains comma separated input values like Adam,99,1,1  making objects using the data, and for adding them to the list.      

`reset()`  

To get ready for a new series of inputs

`process_line()`
 submit, and load both process a line (a string) to generate a student object and to add it to the global list. Package that code into a function, and have submit and load call the function. 

Load is reading comma separated inputs.  Submit accepts inputs separated by space. Both still use the same processline() function.


#### Computing the grade:  
Implement inside the class. 
Specifications:   Graded (A/B)   A >= 80 for lower division, >= 90 for upper division.   Otherwise, B.    Not Graded(PassFail): Pass is >= 40 for both divisions. Otherwise Fail.    

`summary()` 

Summary displays 
Average score
Number of inputs
Average of scores on grade basis
Number of A’s   
Number of 100’s

`Reset and Exit`  
Save data if it needs to be saved, before reset and exit.  

`search()`
Prompts the user to enter a name, and displays matching information if the name is found, displays Not Found otherwise. 





