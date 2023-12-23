#classes and objects in python
class person :    #aise class banate hai 
    name="Proni"; 
    age=19; 
    work='Student'; 
    def display(self):         ##MOST IMPORTANT MOSTLY HAM SELF KO PASS KARTE HAI ARGUMENT KI JAGAH AND HAR JAGAH self.  karke kaam chalate hai
        print(f"The name of the person is {self.name} age is {self.age} and work as a {self.work}");   #use of f strings

a=person();                       #aise objects banate hai 
print(a.name,a.age,a.work);      #aise karke print kar skte hai
a.display(); 


#ek naya object bana kar uske andar changes kiye, so ham bahar v objects k data members k andar changes kar skte hai
b=person(); 
b.name="kriti"; 
b.age=29; 
b.work='developer'; 
b.display(); 

c=person(); 
n=input("Enter your name : "); 
a=input("Enter your age : "); 
w=input("Enter your work : "); 
c.name=n;
c.work=w;
c.age=a; 
c.display(); 