#!usr/bin/python

#File Name: project_11_3.py
#Developer: Martin Hernandez
#Date: 11/27/15
#E-mail: 7607920511m.h@gmail.com
#Description: Write class named Person with data attributes for a person's name,
#address, and telephone number. Next, write a class named Customer that is a
#subclass of the Person class. The Customer class should have a data attribute
#for a customer number and a boolean data attribute indicating whether the
#customer wishes to be on a mailing list. Demonstrate an instance of the
#customer class in a simple program. 

def main():
    name = input('Enter the customer\'s name: ')
    address = input('Enter the customer\'s address, city, state, and zip code: ')
    phone = input('Enter the customer\'s phone number: ')
    number = input('Enter the customer number: ')
    decision = input('Does the customer wish to be on the mailing list? (Y or N): ')
    if decision == 'Yes' or 'yes' or 'YES' or 'Y' or 'y':
        decision = 1
    elif decision == 'No' or 'NO' or 'no' or 'N' or 'n':
        decision = 0
    else:
        print("Invalid Entry")

    customer_account = Person(name,address,phone)
    customer_account.displayPerson()    

    customer_info = Customer(number, decision)
    customer_info.displayCustomer()
    
class Person:
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone

    def displayPerson(self):
        print("\nName: ", self.name, "\nAddress: ", self.address, "\nPhone Number: ", self.phone)

class Customer(Person):
    def __init__(self, number, decision):
        self.number = number
        self.decision = decision

    def __bool__(self):
        if self.decision == 1:
            decision = 'Yes'
        else:
            decision = 'No'
        
    def displayCustomer(self):
        if self.decision == 1:
            self.decision = 'Yes'
        else:
            self.decision = 'No'
        print("\nCustomer Number:", self.number, "\nCustomer decision to be on the mailing list:", self.decision)

main()
