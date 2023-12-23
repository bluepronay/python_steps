#decorators in python

def greet(func):      #it is taking another func as a argument
    def modified():                #another modified function which is decorating the function which is present in argument
        print("Good Morning....\n")      #uss func k call hone se pehle ye print hoga
        func()                           #maine func ka kaam ab kiya
        print("\nThanks for using this function")              #aise hi maje maje mai laga diya
    return modified                          #modified khatam

@greet              #1st and best way to decorate a function , @decorator laga do , fir jab v call karo to decorated answer hi aayega
def hello():
    print("Hello!")

# Calling the decorated function
hello()

def hi():
    print("Hii"); 

greet(hi)()                #another way to call a decorator, second bracket is if the argumented function takes a argument


#NOTE WHAT IF MY FUNCTION IS ALSO TAKING A ARGUMENT

def bigdecorator(func):
    def bigmodified(* args,**kwargs):
        print("The big decorator welcomes you....\n"); 
        func(*args,**kwargs); 
        print("\nA very big byee from big decorator...."); 
    return bigmodified; 


@bigdecorator
def add(a,b):
    print(a+b); 

add(3,5); 

def sub(a,b):
    print(a-b); 

@bigdecorator         #sabse pehle ye call hoga , iske andar arguments jayenge , then vaha se uske andar average function k andar arguments jayenge
def avg(* nums):
    sum=0; 
    for i in nums:
        sum=sum+i; 
    print(sum/len(nums)); 


bigdecorator(sub)(5,2);      #maine isko decorator se nhi banaya tha that's why ab aise arguments pass karne pad rhe hai

avg(4,5,3,7,4,2);             #aise karke maine boht sare arguments diye isko 
