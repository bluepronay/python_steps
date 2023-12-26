#WALRUS OPERATOR IN PYTHON
#new in python not necessary to use , just if you want to decrease the lines of code in your program

a=True; 
print(a); 
print(a:=False); #aise assign karte hai
print(a)

#another use
no=[1,2,3,5,8]; 
while(n:=len(no)>0):  #yha v assign kiya length of list ko
    print(no.pop()); 


#ISKE LINES OF CODE DEKHO
food=list(); 
while True:
    choice=input("Enter your fav food or quit to leave : "); 
    if(choice=="quit"):
        break;
    food.append(choice); 
print(food); 

#ISKE LINES OF CODE DEKHO , WALRUS OPERATOR USE KARNE K BAAD
food=list(); 
while(choice:=input("Enter your fav food or quit to leave : "))!="quit":
    food.append(choice); 
print(food); 