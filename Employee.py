class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

def main():
    person = Employee("Martin", 35)

    print("%s and %s" % (person.name,person.number)
