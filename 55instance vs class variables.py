#INSTANCE VARIABLES VS CLASS VARIABLES
class student : 
    college="SKIT"      #these are class variables, these are same for every objects(instances) which will be created
    branch="AI"          #we can modify the class variables as per my requirement in the code , but by default these two values are given
                         #class variables are defined outside any method
    def __init__(self,n,r):
        self.name=n                #these two are instance variables, which are different for different objects
        self.roll=r
    def show(self):
        print(f"{self.name} is a student of the {self.branch} and is pursuing b.tech from {self.college} college his roll no is {self.roll}\n"); 


st1=student("Pronay",33); 
st2=student("Sanidhya",45); 
st1.show(); 
st2.show();  #dono ka college and branch to same hi aaya na
#now i want to create another object whose name is harshlata from cs branch 
st3=student("Harshlata",88); 
st3.branch="CS";    #i updated the class variable

#now i want to create another object whose college is POORINIMA AND BRANCH IS MECHANINCAL
st4=student("Ritesh",66); 
st4.branch='mechanincal'; 
st4.college='POORNIMA';    #i again updated the class variable
st3.show(); 
st4.show(); 

#so simple si baat yeh hai ki show() method sabse pehle ye dekhega ki kya iska khud ka koi value de rkha hai kya variables ko
#agar maine de rkha hai like poornima , mechanical or cs branch then badhiya varna by default hi chalega 