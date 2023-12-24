#ACCESS SPECIFIERS IN PYTHON

class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age    # Protected attribute
        self.__password = "abc123"  # Private attribute

    def show_public_data(self):
        # Public method
        print(f"Public: Name: {self.name}")
        print(self.__password)          #mai private attribute ko public method se print kara skta hu
        print(self._age)

    def _show_protected_data(self):
        # Protected method
        print(f"Protected: Age: {self._age}")

    def __show_private_data(self):
        # Private method
        print(f"Private: Password: {self.__password}")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing public attributes and methods is straightforward
person.show_public_data()  # Can be accessed outside the class

# Accessing protected attributes/methods conventionally should be avoided outside the class
person._show_protected_data()  # Accessible but a convention to treat as protected

# Attempting to access private attributes/methods from outside the class will result in an error
# person.__show_private_data()  # This will raise an AttributeError

# However, name mangling is used to access private attributes indirectly

#CONCEPT OF NAME MANGLING HAM PRIVATE KO BAHAR ACCESS KAR SKTE HAI PAR USKE LIYE HAME AISE CALL KARNA PADEGA 
#ISKA EK PARTICULAR SYNTAX HAI, VAISE TO NHI KARNA CHAHIYE
print(f"Accessing private attribute: {person._Person__password}")  # Name Mangling (Not recommended)
print("Calling private function :"); 
person._Person__show_private_data();    #aise private function ko call karte hai, vaise nhi karna chahiye
