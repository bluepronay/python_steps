#constructors in python 
'''
pichle part mai hamne andar hi data members ko define kar rkha tha 
iss baar ham unhe ya to kisi constructor k andar rkh k values assign karayenge
'''


#DEFAULT CONSTRUCTORS
class msg : 
    def __init__(self) :
        self.name='proni'         #aise self.name karke ham values assign krte hai
        print("Hello bachoo"); 

a=msg();   #jab v ham is class ka object banayenge to jo v constructor k andar hoga vo khud v khud execute hoga 
b=msg(); 
c=msg(); 
print(a.name); 
print(b.name); 
c.name='kriti'; 
print(c.name); 


#PARAMETERISED CONSTRUCTORS
class person : 
    def __init__(self,n,a,w):
        self.name=n;
        self.age=a;
        self.work=w;
    
    def info(self):
        print(f"The name of the person is {self.name} age is {self.age} and work as a {self.work}");

a=person("Proni",19,'Student');    #arguments pass kiya

a.info(); 
 
n=input("Enter your name : "); 
a=input("Enter your age : "); 
w=input("Enter your work : "); 
b=person(n,a,w);           #arguments pass kiya
b.info(); 

b.name='bhalu'    #baad mai v changes kar skte hai
b.info(); 

# c=person();    ye error dega bcoz koi v arguments pass nhi kiye , hamko total teen arguments pass karne hai iss example mai
#hamne constructors banate time 4 argument liye hai but hame yaha 3 hi karne hai as ek argument khud self hai

#self argument khud k object ka argument hota hai jis par dot lagakar ham uske data members ko values assign karte hai