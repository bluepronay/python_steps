#CLASS METHODS
'''
class method is not like static method, it takes the class as the argument, not an instance 
like other methods of a class , and we can change the value of different class variables from that method
IT IS IMPORTANT TO NOTE THAT I AM TALKING ABOUT CLASS VARIABLES , NOT INSTANCE VARIABLES
'''
class Employee:
    company="Apple"; 
    location="India"; 
    def __init__(self,n,id) :
        self.name=n
        self.id=id
    def show(self):
        print(f"The name of the employee is {self.name} from {self.company} {self.location} and his id is : {self.id}"); 

 #this method can change the company name of the whole class    
    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany
#this method can change the location of the whole class
    @classmethod
    def changelocation(cls,newlocation):
        cls.location=newlocation

e1=Employee("Proni",23); 
e1.show(); 
#let's change the company of e1 only
e1.company="Google"; 
e1.show(); 
#abhi tak sirf proni ka company change hua hai
print(Employee.company); #yha abhi v apple hi aayega as class ka to abhi v apple hi hai , vo to bas ek object ka change hua hai

#another object
e2=Employee("Sani",44); 
e2.changecompany("Infosys"); #ab sani ka hi nhi har ek object jo ab banega uska company infosys hai
e2.show(); 
e1.show(); 
print(Employee.company); 
e3=Employee("rani",33); 
e3.changelocation("US");   #maine ab company ki default location hi badal di , ab sabka us aayega
e1.show();          #proni ka google hi rahgega bcoz maine uska manually change kiya tha
e2.show(); 
e3.show(); 
Employee.changecompany("Cognizant");  #mai aise v change kar skta hu seedha class k saath call karke , as ye class method hai
e1.show(); 
e2.show(); 