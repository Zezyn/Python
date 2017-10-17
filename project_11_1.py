#!usr/bin/python

#File Name: project_11_1.py
#Developer: Martin Hernandez
#Date: 11/22/15
#E-mail: 7607920511m.h@gmail.com
#Description:
#Employee and ProductionWorker Classes
#Write an employee class that keeps data attributes for the following pieces of information:

 #Employee  name
 #Employee number

#Next, write a class named ProductionWorker  that is a subclass of the Employee class.   the
#ProductionWorker class  should keep data attributes for the following information:

 #Shift number( and integer,  such as 1, 2, or 3)
 #Hourly   pay rate

#The workday is divided into two shifts:  day and night.   The shift attribute will hold an
#integer value representing the shift that the employee works.   The day shift is shift 1 and
#the night shift is shift 2.   Write the appropriate accessor and mutator methods for each class. 

#Once you have written the classes, write a program that creates an object of the ProductionWorker
#class and prompt the user to enter data for each of the object's data attributes.
#Store the data in the object and then use the object's accessor methods to retrieve it and display it on the screen.

def main():
    name = input('Please enter the employee name: ')
    number = int(input('Please enter the employee number: '))
    shift = input('Please enter the employee\'s shift: (Day or Night) ')
    if shift == 'night' or 'NIGHT':
        shift = 'Night'
    else: shift = 'Day'
    pay = float(input('Please enter the employee\'s pay rate: '))

    emp1 = Employee(name, number)
    emp2 = ProductionWorker(shift, pay)

    print("Employee details:")
    emp1.displayEmployee()
    emp2.displayWorker()
    
class Employee:
    
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def displayEmployee(self):
        print("\nName: ", self.name, "\nNumber: ", self.number)

class ProductionWorker(Employee):
    def __init__(self,shift,pay):
        self.shift = shift
        self.pay = pay

    def displayWorker(self):
        print("\nShift: ", self.shift, "\nPay: ", self.pay, "\n")
        
main()
