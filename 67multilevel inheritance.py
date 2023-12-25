#MULTILEVEL INHERITANCE 
#ek class ka child , and uska v child simple logic 
#isse lines of codes kitna kam ho chuke hai dekhna
class base : 
    def __init__(self,n,a):
        self.name=n; 
        self.age=a; 
    def show(self):
        print(f"Name is {self.name} and age is {self.age}"); 

class derived1(base):
    def __init__(self, n, a,br,r):
        super().__init__(n,a)   #base class constructor called
        self.branch=br; 
        self.roll=r; 
    def show(self):
        super().show();   #base class show called 
        print(f"Branch is {self.branch} and roll no is {self.roll}"); 

class derived2(derived1):
    def __init__(self, n, a, br, r,com,sal):
        super().__init__(n, a, br, r);   #derived1 constructor called
        self.company=com; 
        self.salary=sal; 
    def show(self):
        super().show()  #derived1 show called
        print(f"Company is {self.company} and salary is {self.salary}"); 


e=derived2("Proni",19,"AI",33,"Infosys",50000);   #ek hi class mai sare attributes pass kar diye,ab uska constructor hi baakiyo ko bula lega
e.show();   #ek hi show se teeno show call ho jayenge
print(derived2.mro());   #ye priority batayega agar same naam k function teeno class mai ho to 


     
        

        
        