#typecasting 
"""
two types of typecasting 
explicit if i am changing 
implicit if the python is converting a int into float 
so the data is not lost 
it will convert the lower priority data type into higher priority data type

"""
a='115';
b='2';
c=100;
d=10.33;
print(a+b);    #it is concatenating strings
print(int(a)+int(b));   #explicit type casting converted the string into integer
print(c+d);           #implicit type casting by python
#i can't do a="Harry"  and b=1 and think a+b will run it will show error

