#static and global variables
x=4;

def printx():
    x=6; 
    print(x); 

printx();    #6 aayega
print(x);   #4 aayega

def printxglobal():
    global x;
    x*=6; 
    print(x); 
   
printxglobal(); #aise global use karte hai kisi function mai