#HIERCHICAL INHERITANCE
#KHUD PADHLE YRR , ITNA TO PATA HONA CHAHIYE
# Parent class
class Animal:
    def sound(self):
        print("Some generic sound")


# Child classes inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Woof woof!")


class Cat(Animal):
    def meow(self):
        print("Meow!")


# More child classes inheriting from Dog and Cat
class Labrador(Dog):
    def breed_info(self):
        print("Labrador: A friendly and playful breed!")


class PersianCat(Cat):
    def breed_info(self):
        print("Persian Cat: Known for its long fur and sweet temperament!")


# Instances of the new classes
labrador = Labrador()
persian_cat = PersianCat()

# Accessing methods from different classes
labrador.bark()  # Output: Woof woof!
persian_cat.meow()  # Output: Meow!

# Accessing unique methods of the new classes
labrador.breed_info()  # Output: Labrador: A friendly and playful breed!
persian_cat.breed_info()  # Output: Persian Cat: Known for its long fur and sweet temperament!
labrador.sound(); #output : some generic sound  (topmost class ka method)
