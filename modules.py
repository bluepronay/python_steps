#modules in python
#modeules ko import karke ham unke functions ka use karne k liye module name k saath dot lagake use karte hai

# to import a module import is used
import math;
x=9;
y=math.sqrt(x); 
print(y)


#if we want a particular function to be imported from a module we do from module name import function name 
from time import strftime;
t=strftime('%H'); 
print(t)
#when we import a particular fun then we don't need to use the dot structure

# z=sqrt it is wrong


# i can import many modules and many function using a comma sign between them 
#similarly if i don't want that i have to write the full name of the function then i can use the "as" keyword 
#this as is same as the typedef keyword in c
from time import strptime as s;
s("30 Nov 00", "%d %b %y")   

#i can import inbuilt files from my local desktop here so that i can use the functions from there

from sum import sumterms as s;
x=s(7); 
print(x)

from sum import fact as f;
y=f(5); 
print(y)

import proni
proni.welcome()       #aise v use kar skte hai

