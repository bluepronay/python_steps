#functions in python two types inbuilt and userdefined
#def keyword is used 
#pass keyword is used if we want to skip the body of the function for some time

def mean(a,b,c,d,e):
    sum=a+b+c+d+e; 
    sum=sum/5;             #yha v indented ka rule lagta hai
    print(sum); 

def product(a):
    pass           #mereko nhi likhna body that's why pass keyword use kiya

def factorial(a):
    prod=1; 
    for i in range(1,a+1):               #indentation ka dhyan rakhna hi padega
        prod*=i; 
    print(prod)
 

a=int(input('Enter no : ')); 
b=int(input('Enter no : ')); 
c=int(input('Enter no : ')); 
d=int(input('Enter no : ')); 
e=int(input('Enter no : ')); 
mean(a,b,c,d,e); 

factorial(a); 