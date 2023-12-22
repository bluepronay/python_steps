#fstrings in python new feature

name=input("Enter name");
pos=input("Enter the position");
clg=input("Enter the clg name");
age=int(input("Age ")); 
#input le liya

#ye syntax hai kisi string k andar aisa karlo 
sent="Hello, guys, my name is {name},{age}years old and I am the {pos} of {clg} welcoming you all"; 

#aise value assign kar skte hai
print(sent.format(name=name,pos=pos,clg=clg,age=age)); 

sent1="hii I am {name}";
n=input("Enter the name : ");    
print(sent1.format(name=n)); 
print(sent1);                    #aise to nhi hoga


#if i don't want to form a string and directly want to print the sentence i can use f before the "" so that which means it is formating
print(f"Hii I am good boy whose name is {name}, I am {age} years old from the college {clg}");

price=19.45636663  #a floating value
print(f"the price of milk is {price:.4f}")          #price:.3f is used so that i can print two decimals 

#if i genuinly want to print {name} in the print statements if f is there than i have to use {{name}} at this {name} will be printed
print(f"To use the fstring in python the required format is {{name}} and {{age}},in this way we print");