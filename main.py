''' University Department System Management'''
'''Author: Roshini Ghanta 
   Student ID: GH1060113'''

import Uni_sys_classes as uni

def main():

    while True:

        print("Welcome!")
        print('1. Register a Student')
        print('2. End')
        choice= input('Enter your choice(1,2):')

        if choice == '1':
            
            first_name = input('Enter your first name:')
            last_name = input('Enter your last name:')
            age= int(input('Enter your age:'))
            ID_number= input('Enter your ID number:')
            email_address= input('Enter your email address:')

            student1= uni.Student(first_name,last_name,age,ID_number,email_address)
            student1.register_student(first_name,last_name,age,ID_number,email_address)
            print(student1)

        if choice == '2':
            print ('Thank you')
            break


    


if __name__ == '__main__':                  # If the name of the file is '__main__', then if condition is True and will execute
    main() 