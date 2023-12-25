#it is the emp.py which i am using here i am emporting that class here
# class Employee:

#   def __init__(self, name):
#     self.name = name

#   def __len__(self):
#     i = 0
#     for c in self.name:
#       i = i + 1
#     return i

#   def __repr__(self):
#     return f"Employee('{self.name}')"

#   def __str__(self):
#     return f"The name of the employee is {self.name} str"

#   def __call__(self):
#     print("Hey I am good")

from emp import Employee  #imported

e = Employee("Harry")
print(str(e)) #aise call karte hai dunder functions ko 
print(repr(e))
# print(e.name)
# print(len(e))
e()     #ye wala seedha object se call laga diya 
print(len(e))
# print(e.len());   #aise nhi karna hai 
print(e)

#NOTE THEREFORE DUNDER METHODS
# Dunder (double underscore) functions, also known as special or magic methods in Python,
# are used to enrich classes with specific functionalities that can be invoked by special syntax or operations. 
#They are surrounded by double underscores at the beginning and end of their names (e.g., __init__, __repr__, __add__).