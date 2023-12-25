#SUPER KEYWORD IN PYTHON
#this keyword is used to call the function of the parent class in its child class
#syntax is super().

class person:      #made a person class
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print(f"Name of the person is : {self.name},person's age is {self.age}"); 
    def hello(self):
        print("Hello from parent class....");

class student(person):       #inheritance done
    def __init__(self,n,a,r,br):
        super().__init__(n,a);        #called the constructor of parent class, so that name and age can be passed there 
        self.roll=r; 
        self.branch=br; 
    def show(self):           
        super().show();        #called the parent class function to reduce line of codes
        print(f"Student's roll no is {self.roll} and the branch is {self.branch}"); 
    def hello(self):
        print("Hello from child class...."); 

st1=student("Harry",19,33,"AI"); 
st1.show(); 
st1.hello();  #called the child class function
person.hello(st1); #u can call the parent class function for a particular object in this way if you want to
        
#NOTE IF THERE ARE SAME FUNCTION NAME IN CHILD AND PARENT CLASS AND WE CALL THAT FUNCTION BY CHILD CLASS THEN CHILD CLASS FUNCTION WILL BE CALLED

        