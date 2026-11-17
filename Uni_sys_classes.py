class Student:

    """ This class stores student information 
    Attributes= fname: str, lname: str, age: int, student_number: str, student_email: str, students: dict, number_of_students: int
    Methods= verify_age(), full_name(), verify_email(), verify_student_number(),register_student(), add_to_number_of_students() """ 

    number_of_students = 0

    @classmethod
    def add_to_number_of_students(cls):

        ''' This method updates the number of students registered'''

        cls.number_of_students += 1

    # INIALIZATION OF THE ATTRIBUTES 
    def __init__(self,fname,lname,age,student_number,student_email):

        ''' This method initializes the attributes of the class'''

        self.fname=fname
        self.lname=lname
        self.age=self.verify_age(age)
        self.student_number=self.verify_student_number(student_number)
        self.student_email=self.verify_student_email(student_email)
        self.students={}
        Student.add_to_number_of_students()

    # METHODS FOR VERIFICATION 
    def verify_age(self,age):

        """ This method check if the age inputed is valid """

        if isinstance(age,int) and age>0 and age<100:
            self.age=age
        else:

            """ Here, it prints an error message when if statement is not true """

            print('Cannot accept this age!')

    def verify_student_number(self,student_number):

        """ This method checks if the student number inputed is valid """

        if student_number[0:2] != 'GH':

            """ Error message when if statement is false """

            print('Cannot accept this student number!')

        else:

            self.student_number=student_number

    def verify_student_email(self,student_email):

        """ This method checks the validity of the email provided """

        split_student_email= student_email.split('.')

        if split_student_email[-1] == 'com':
            self.student_email=student_email

        else:

            """ Error message when if statement is false """

            print('Cannot use this email!')
            
    # METHOD FOR STORING STUDENT DATA
    def register_student(self,fname,lname,age,student_number,student_email):

        """ This method stores the information provided in a disctionary"""

        self.students[student_number] = {
            'name': self.full_name(fname, lname),
            'age': self.age,
            'email': self.student_email
            }

    # METHOD FOR GENERATING FULL NAME
    def full_name(self,fname,lname):

        """ This method generates the full name of the student """

        return f'{fname} {lname}'
    
    # METHOD FOR DISPLAYING STUDENT INFORMATION
    def __str__(self):

        """ This method generates an output for the print statements.
        In this case, it prints the dictionary and the number of students registered """

        
        return f'Students:{self.students} and Total:{Student.number_of_students}'
    

