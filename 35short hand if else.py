#short hand if else statements
a=333;
b=256;
print("A") if(a>b) else print("B") if(b>a) else print("=");   #pehle statement likhte hai 
#pehli baar statement k baad if likhte hai uske baad condition uske baad else fir statement fir if fir condition

#kisi ko value v de skte hai
c="A is greater" if(a>b) else "B is greater" if(b>a) else "Both are ="; 
print(c)
#yha pe c ko string ki value de di 

#note :- ye sirf simpler problems mai hi use karna nested if else mai yeh pagla jata hai

a=int(input("Enter the first no : ")); 
b=int(input("Enter the second no : ")); 
c=a/b if(a>b) else b/a if(b>a) else  87; 
print(c); 