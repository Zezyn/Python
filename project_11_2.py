#!usr/bin/python

#File Name: project_11_2.py
#Developer: Martin Hernandez
#Date: 11/22/15
#E-mail: 7607920511m.h@gmail.com

#Description:
#In a particular factory, a ShiftSupervisor is a salaried employee who supervises a  shift.
#In addition to a salary, the shift supervisor earns a yearly bonus when his or her shift
#meets production goals.   Write a ShiftSupervisor class that is a subclass of the Employee
#class you created in programming exercise 1.    The shift supervisor class should keep a
#data attribute for the annual salary and a data attribute for the annual production bonus
#that a shift supervisor has earned.  Demonstrate the class by writing a program that uses
#a ShiftSupervisor object.

def main():
    name = input('Please enter the employee name: ')
    supervisor = input('Is the employee a supervisor? (Y or N): ')
    number = int(input('Please enter the employee number: '))
    shift = input('Please enter the employee\'s shift: (Day or Night) ')
    if shift == 'night' or 'NIGHT':
        shift = 'Night'
    elif shift == "day" or "DAY":
        shift = 'Day'
    else:
        print("Invalid")
        exit

    if supervisor == 'Y' or 'y' or 'yes' or 'YES' or 'Yes':
        pay = float(input('What is the supervisor\'s annual salary? '))
        bonus = float(input('What is the supervisor\'s annual bonus?'))
        super = ShiftSupervisor(pay, bonus)
        super.displaySupervisor()
    elif supervisor == 'N' or 'n' or 'no' or 'No' or 'NO':
        pay = float(input('Please enter the employee\'s pay rate: '))
        emp2.displayWorker()
    
    else:
        print('Invalid Entry')
        exit

    emp1 = Employee(name, number)
    emp2 = ProductionWorker(shift, pay)
    emp1.displayEmployee()
                      
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

class ShiftSupervisor(Employee):
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus

    def displaySupervisor(self):
        print("\nSalary: ", self.salary, "\nBonus: ", self.bonus)
        
main()

