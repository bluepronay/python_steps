#recursion
#you know very well
def fact(n):
    ''' It will return the factorial of a particular no'''
    if(n==0|n==1):
        return 1; 
    else:
        return fact(n-1)*n; 

def fib(n):
    '''It will return the n'th letter of the fibonnaci series'''
    if(n==1 or n==2):
        return 1;
    else:

        return (fib(n-1)+fib(n-2)); 

i=int(input("Enter the no : "));
print(fact.__doc__)
print(fact(i));
print(fib.__doc__); 
print(fib(i));