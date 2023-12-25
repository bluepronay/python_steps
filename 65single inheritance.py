#SINGLE INHERITANCE   #inheritance wale code ko hi repeat kiya hai nothing else
class Person:
    def __init__(self, n, a):          #made a constructor
        self.name = n
        self.age = a

    def show_details(self):
        print("The name of the person is:", self.name, "Age is:", self.age)


class Employee(Person):                    #this is how you do inheritance in python
    def __init__(self, id, pos, n, a):
        super().__init__(n, a)  # Call the parent class constructor        it is the most important line 
        self.id = id
        self.position = pos

    def show_emp(self):
        print(f"The Employee ID is: {self.id} Position: {self.position}")     #i can use fstrings also


name = input("Enter your name: ")
age = int(input("Enter your age: "))
id = int(input("Enter your ID: "))
pos = input("Enter your position in the company: ")

emp1 = Employee(id, pos, name, age)
emp1.show_details()
emp1.show_emp()