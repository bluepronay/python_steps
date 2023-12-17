#conditional statements 
#relational operators >,<,>=,<=,==,!= etc
print(5>10); #false batayega
#example of nested if else statement elif use hota hai yaha aur colon ':' use hota hai and the concept of spacing 
# v hai yha pe so dhyan rakhna
a=int(input("Enter your age : ")); #int mai lega input
if(a>=18) : 
    if(a>25) : 
        print("You can go for election ,drive as well as you can marry");   
    elif(a>21) : 
        print("You can drive as well as you can marry..");       #jo if k neeche aa gya space chod k vo if k andar ka statement hai
    else :                                                                          
        print("You just drive..");
elif(a>15) : 
    print("you are in teenage...");
elif(a>10):
    print("You must be in school...");
else : 
    print("You are still a kid..."); 


