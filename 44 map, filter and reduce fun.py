#map , filter and reduce functions 

#MAP FUNCTION - it is a higher order function, which takes other function as argument , and a iterable object also 
#in this case list is a iterable object , it will return a map object i will typecast it into list and store into a new list
#in this way , in this newlist i have the cube of every element of the list no

def cube(x): 
    return x*x*x; 

no=[1,2,3,4,5,6]; 
new=list(map(cube,no));     #map kiya cube function ka no list k saath, ek map object vapas aaya tha use list mai convert kar diya
print(new); 

#i can use lambda function also , let's do for square
new=list(map(lambda x : x*x,no));    #one liner function
print(new); 


#FILTER FUNCTION - it is a higher order function, which takes other function as argument , and a iterable object also 
#in this case list is a iterable object , it will return a map object i will typecast it into list and store into a new list
#in this way , but here i have to cfreate a filter function which will either return true or false
#if the filter function returns true , then it will store its corresponding value otherwise it will not store

#example i want to store the marks which are greater than 75 
marks=[45,24,88,23,99,100,33,65,57,81,52,96]; 
def filterfunction(x): 
    return x>75; 

new1=list(filter(filterfunction,marks));    #filter function true ya false return karega and marks k element uss hisaab se store honge
print(new1); 
new2=list(filter(lambda x : x%2==0,marks));    #lambda function use kar liya , jo true ya false return karta hai even hone par
print(new2); 


#REDUCE FUNCTION - it is a higher order function, which takes other function as argument , and a iterable object also 
#in this case list is a iterable object , it will return a value , and i have to print it
#in this way , but here i have to import the reduce function from somewhere else

from functools import reduce
no=[1,2,3,4,5,6];  #a list
def sum(x,y): 
    return x+y; 
new3=reduce(sum,no);    #sare elements ka addition kar rha hai
print(new3); 

new4=reduce(lambda x,y : x*y,no);    #lambda fun ka use kar liya and sabka product nikal liya
print(new4); 