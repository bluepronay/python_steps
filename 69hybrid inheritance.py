#HYBRID INHERITANCE 
#KHUD PADH LE YRR MOOD CHALA GYA INHERITANCE KARTE KARTE!!!SORRY....

class Person:
    def greet(self):
        print("Hello, I am a person.")


class Student(Person):
    def study(self):
        print("I am studying.")

    def greet(self):
        super().greet()  # Call the greet method of the parent class
        print("Hello, I am a student.")


class Employee(Person):
    def work(self):
        print("I am working.")

    def greet(self):
        super().greet()  # Call the greet method of the parent class
        print("Hello, I am an employee.")


class Teacher(Employee):
    def teach(self):
        print("I am teaching.")

    def greet(self):
        super().greet()  # Call the greet method of the parent class
        print("Hello, I am a teacher.")


class TeachingAssistant(Student, Employee):
    def assist(self):
        print("I am assisting.")

    def greet(self):
        super(Student, self).greet()  # Call the greet method of Student
        super(Employee, self).greet()  # Call the greet method of Employee
        print("Hello, I am a teaching assistant.")


# Instance of TeachingAssistant and calling all greet functions
ta = TeachingAssistant()
ta.greet()
