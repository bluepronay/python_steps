#sum of n terms from 1;

def sumterms(a):
    sum=0;
    for i in range(a+1):
        sum=sum+i; 
    return sum; 


def fact(a):
    facti=1;
    if(a==0 or a==1):
        return 1; 
    else :
        return a*fact(a-1); 