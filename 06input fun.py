#input function
'''
python takes input in string ,we can take input in int by int(input())  syntax
to take input in single line you have to a,b=input().split()
if you want that it should convert the string into int then do type conversions 
it is similiar to scanf but you can print the sentences which you used to print f before scanf

'''

a=input();
print(a);
b=input();
print(a+b);            #it will do string concatenation
print(int(a)+int(b));
c=input("Enter the First Name : ");          #you can input space also it will take care of it like gets function
d=input("Enter the Last Name : ");
print("Your Name is \"",c,d,"\"");
e=int(input("enter : ")); 
f=int(input("enter : "));
print(e+f); #output print karega

