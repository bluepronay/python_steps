#for loops in python
'''
it can be used to print the strings or lists 
it can be used with the range function which has the basic syntax of 
range(start,stop,step(operation))
all three arguments are integer start is by default =0,stop is excluded, step is by default +1
range(stop) is necessary
range(start,stop ) is possible
range(start,stop ,step )is also possible
'''

name="Pronay";
print(name);
for i in name : 
    print(i)   #it will print in new line
for i in name : 
    print(i,end="");  #it will print in single line as end is there
print("\n");
colorlist=["Red","Blue","Green","yellow"];        
for i in colorlist :            #red blue green will be on new line
    print(i)

for i in colorlist :                  #i ab colorlist ka element hai which means ek element at a time
    for j in i :                       #j ab i ka element hai 
        print(j);                       #har ek alphabet ko next line mai print karayega

#range function

for i in range(6):         #with stop only
    print(i)              #0 se 5 tak

for i in range(1,6) :                   #with start and stop
    print(i)                     #1 se leke 5 tak

for i in range(1,15,2):               #sare odd no 
    print(i)
    if(i==9) : 
        print("it is nine");