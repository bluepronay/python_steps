#lambda functions in python
#these functions are anonymous it is not necessary that they should have names
#in python there are many places , when we have to use many small functions where we have to write the function body 
#one line only, at that place to reduce the lines of codes we use lambda functions

def double(d): 
    return d*2; 

#syntax of lambda if we are defining, function name = lambda arguments : return statement (no return keyword is used)

dob=lambda x : x*2;    

avg=lambda x,y : (x+y)/2;    #one liner functions  

print(double(2)); #4 aayega
print(dob(2));   #4 aayega
print(avg(7,2));   #4.5 aayega

#best use of lambda functions , we can use lambda function in a higer order function also 
#higher order functions are those functions which take other functions as their arguments, for this in the statement, we just have to write the lambda functions without specifying their names
#that's why lambda functions sometimes don't have any name

def higherorder(fx,n): 
    return 6+fx(n); 

print(higherorder(lambda x : x*x*x,4));  


# higerorder fn ko call kiya, fir lambda fun pass kiya
#iske definition mai ham kisi ek argument ka cube kar rhe hai
#higerorder fun mai hamne n k cube se 6 add kr diya therefore ans is 70


print(higherorder(lambda t : t*4,8))  #one more passing of lambda function

