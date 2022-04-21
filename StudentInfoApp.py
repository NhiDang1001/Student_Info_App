"""Homework 7. Developed by Nhi Dang. 03.09.2021. """

#globals
students = [] #a global list of students 
studentsdict = {}  #a dictionary to speed up search  key:name  value:score, status_str, division_str   student object
filename = '' #use in the save(), promt the user to enter filename only once
need_to_save = False #whether to save or not
saved_student = [] #a list of saved students

#functions

class Student:

    #class variables
    total_score = 0.0
    count = 0
    total_graded_score = 0.0  #total graded score
    count_graded = 0   #count of graded score
    count_A = 0
    count_100 = 0
    
    def __init__(self, name, score, status_str, division_str):
        self.name = name
        self.score = score
        self.status_str = status_str
        self.division_str = division_str 
        self.grade = self.computegrade()

        #updates totals
        Student.total_score += self.score
        Student.count += 1
    
        if self.status_str == 'Graded':
            Student.count_graded += 1
            Student.total_graded_score += self.score
        
    
    def compute_grade(self):
        if (self.score >= 80 and self.division_str == 'Lower') or (self.score >= 90 and self.division_str == 'Upper'):
            self.grade = 'A'
            Student.count_A += 1
            if self.score == 100:
                Student.count_100 += 1

        else:
            self.grade = 'B'
        return self.grade

    def compute_passfaill(self):
        if self.score >= 40:
            self.grade = 'P'
        else:
            self.grade = 'F'
        return self.grade    

    def computegrade(self):
        if self.status_str == 'Graded':
            self.grade = self.compute_grade()
        else:
            self.grade = self.compute_passfaill()
        
        return self.grade

    
    def __str__(self):
        return f'{"Name:":s} {self.name:s} | {"Score:":s} {self.score:.2f} | {"Status:":s} {self.status_str:s} | {"Division:":} {self.division_str:s}| {"Grade:":} {self.grade:s} '
    
    def display_line(self):
        return f'|{self.name:12s}|{self.score:^12.2f}|{self.status_str:^12s}|{self.division_str:^14s}|{self.grade:^12s}'
    
    def save_line(self):
        return f'{self.name:12s},{self.score:^12.2f},{self.status_str:^12s},{self.division_str:^14s},{self.grade:^12s}'
    
    @classmethod
    def compute_average(cls):
        return cls.total_score / cls.count if cls.count > 0 else None
    
    @classmethod
    def compute_average_graded(cls):
        if cls.count_graded > 0:
            return cls.total_graded_score / cls.count_graded
        else:
            return None 
    
    @classmethod
    def reset_data(cls):
        cls.total_score = 0.0
        cls.count = 0
        cls.total_graded_score = 0.0
        cls.count_graded = 0

    @classmethod
    def summary_string(cls):
        average_score = cls.compute_average()
        average_graded_score = cls.compute_average_graded()
        out_string = ''
        if average_score is not None:
            out_string += f'Average score:{average_score:.2f}\nCount:{cls.count}' + '\n'
            if average_graded_score is not None: 
                out_string += f'Average graded score:{average_graded_score:.2f}\nGraded count:{cls.count_graded}\nNumber of A:{cls.count_A}\nNumber of 100s:{cls.count_100} '
        else:
            out_string += 'No data'
        
        return out_string 

#end class
def is_valid_score(score):
    return 0 <= score <= 100
def is_valid_status(status):
    return status == 1 or status == 0

def is_valid_division(division):
    return division == 1 or division == 0

def process_line(line, separator = None):
    global students, studentsdict, need_to_save

    in_list = line.split(separator)
    name = in_list[0]
    score = float(in_list[1])

    while not is_valid_score(score):
        print('Error')
        score = float(input('Enter score in range 0..100: >>'))


    status = int(in_list[2])
    
    while not is_valid_status(status):
        print('Error')
        status = int(input('Enter 1 for Graded or 0 for Pass/Fail status: >>'))


    division = int(in_list[3])

    while not is_valid_division(division):
        print('Error')
        division = int(input('Enter 1 for Upper or 0 for Lower division: >>'))
    
    if status:
        status_str = 'Graded'
    else:
        status_str = 'Pass/Fail'
    
    if division:
        division_str = 'Upper'
    else:
        division_str = 'Lower'   
    
    student = Student(name, score, status_str, division_str)
    students.append(student)
    studentsdict[student.name] = student 
    need_to_save = True

    return student 



def submit():
    global students
    
    line = input('Name, score, graded or passfail(1/0), upper or lower division(1/0): >>')
    student = process_line(line)

    print(student)


def load():
    global students
    filename = 'in_data.txt'

    with open(filename,'r') as infile:
        lines = infile.readlines()
    
    for line in lines:
        process_line(line, ',')

    print(f'{len(lines)} student records loaded')

def summary():
    global students
    print(Student.summary_string())

def reset():
    clear_data()
    Student.reset_data()

def line():
    print('-'*65)

def display():
    global students
    
    if students:
        line()
        print(f'|{"Name":12s}|{"Score":^12s}|{"Status":^12s}|{"Division":^14s}|{"Grade":^12s}')  
        line()
        for student in students:
            print(student.display_line())
    else:
        print('Nothing to display!')

def save():
    global students, studentsdict, filename, need_to_save, saved_student
    if filename == '':
        filename = input('Enter a file name: >>')

    if need_to_save:
        with open(filename, 'a') as outfile:
            for student in students:
                if student not in saved_student:
                    outfile.write(student.save_line()+'\n')
                    saved_student.append(student)
        print(f'All data saved...{len(students)} students record saved to file. ')
        students.clear()
        need_to_save = False
    else:
        print('Not Save!')

def search():
    global students, studentsdict
    
    name = input('Enter a name to search for: >>')
    found = 0
    for student in students:
        if student.name == name:
            found = 1
            print('Found!')
            print(student)
            break 
    
    if not found:
        print('Not found')
    
    

def search_by_dict():
    global studentsdict

    key = input('Enter a name to Fast Search: >>')

    if key in studentsdict.keys():
        print('Found!')
        print(studentsdict[key])
    else:
        print('Not Found!')

def clear_data():
    global students, studentsdict
    students.clear()
    studentsdict.clear()


#main
quit = False
while not quit:
   print('1.Submit 2.Load 3.Summary 4.Display 5.Save 6.Search 7.Fast Search 8.Reset 9.Exit')
   choice = int(input('Enter choice:  '))
   if choice == 1:
       submit()
   elif choice == 2:
       load()
   elif choice == 3:
       summary()
   elif choice == 4:
       display()
   elif choice == 5:
       save()   
   elif choice == 6:
       search()
   elif choice == 7:
       search_by_dict()
   elif choice == 8:
       reset()
       print('Data cleared. Ready for new series..') 
   elif choice == 9: 
       quit = True   
       clear_data()
   else:
       print('Invalid Choice!')

print('Bye!!!')