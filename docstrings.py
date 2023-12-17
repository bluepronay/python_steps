#docstrings in python
#used to tell the description of any function,class,module,block,etc
#it should be added before the function body otherwise it will not work 
#it adds a attribute property to that , which can be accessed letter
#similiar to comments but is not ignored if accessed;,only triple quotes are used

def square(a):
    ''' it is used to calculate the square of a particular no
    '''
    return a*a; 

i=int(input()); 
print("The square is", square(i)); 
#to access
print("the discription is",square.__doc__);   #__doc__ is used