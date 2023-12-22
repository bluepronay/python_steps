#docstrings in python
#used to tell the description of any function,class,module,block,etc
#it should be added before the function body otherwise it will not work 
#it adds a attribute property to that , which can be accessed letter
#similiar to comments but is not ignored if accessed;,only triple quotes are used

def square(a):
    ''' it is used to calculate the square of a particular no
    '''
    return a*a; 
def factorial(a):
    '''I will calculate the factorial of a no 
    '''
    if(a==1 or a==0):
        return 1; 
    else :
        return a*factorial(a-1);
i=int(input()); 
print("The square is", square(i)); 
#to access
print("the discription is",square.__doc__);   #__doc__ is used
print("The description is ",factorial.__doc__,factorial(i)); 
