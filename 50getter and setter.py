'''
Getters in Python are methods that are used to access the values of an object's properties. 
They are used to return the value of a specific property, and are typically defined using the @property decorator. 
Here is an example of a simple class with a getter method:
In this example, the MyClass class has a single property, _value, which is initialized in the init method. 
The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.

To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:

Setters
It is important to note that the getters do not take any parameters and we cannot set the value through getter method.
For that we need setter method which can be added by decorating method with @property_name.setter
In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. 
This can be useful for encapsulation and data validation.
'''

class MyClass:
  def __init__(self, val):
      self.value = val
    
  def show(self):
    print(f"Value is {self.value}")
    
  @property           #we use property decorator for getter
  def ten_value(self):       #getter    now ten_value is also a data member or attribute
      return 10* self.value
    
  @ten_value.setter                #@attribute.setter se ham setter banate hai, isspe ham getter wali value lete hai ,
  def ten_value(self, new_value):
      self.value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()