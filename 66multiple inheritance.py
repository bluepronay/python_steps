#MULTIPLE INHERITANCE 
#MANY PARENTS K SAME CHILD....

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student:
    def __init__(self, school, roll_no):
        self.school = school
        self.roll_no = roll_no

    def show(self):
        print(f"School: {self.school}, Roll No: {self.roll_no}")


class Employee(Person, Student): #syntax to declare multiple inheritance
    def __init__(self, name, age, company, emp_id, school, roll_no):
        Person.__init__(self, name, age)
        Student.__init__(self, school, roll_no)
        self.company = company
        self.emp_id = emp_id

    


# Creating an Employee object
emp = Employee("John Doe", 30, "XYZ Corp", "E123", "ABC School", "S456")

# Calling show method
emp.show()  #dekho sahi se abhi sirf person class ka hi call hoga, bcoz hamne person class ko pehle parent banaya hai
Student.show(emp)     #aise karke ham iss studnet class k show() ko call kar skte hai as ye second priority hai

print(Employee.mro()); #ye hame priority batata hai 
#agar teen functions same naam k teeno class mai hai then konsi wali pehle call hogi
#pehle child class mai vo function hai to vahi call ho jayegi
#dusra agar child mai nhi hai to jo pehla parent bana hai declare karte time vo call hogi 
#teesra agar pehle parent mai v vo function nhi hai to second parent ka function call ho jayega
#iss case mai child employee hai , pehla parent person and dusra parent is student
