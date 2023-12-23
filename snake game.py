#SNAKE , WATER AND GUN GAME
import random; 
import os; 
import time;

# Generate a random integer between 1 and 10 (inclusive)
ra_no = random.randint(1,3)
print(ra_no)
time.sleep(1); 
os.system("cls"); 
well="SNAKE,WATER AND GUN GAME"; 
print(well.center(80,'*')); 
rules='''You have 30 seconds to read the rule
First of all you have options of three kind of matches
1. 3
2. 5
3. 7
4. Exit
You have to select any one of them
If you win more than half matches then you win the game
Best of Luck
'''

gamerules='''
(i)   Snake beats Water
(ii)  Water beats Gun
(iii) Gun beats Snake
'''

print(gamerules); 
choice='''
1. Snake
2. Water 
3. Gun
'''
print(choice)
while True :
 print(well.center(80,'*')); 
 print(rules); 
 ch=int(input("Enter your match mode : "));
 match ch : 
  case 1 :
     win=0; 
     valid=0;
     while True : 
      os.system("cls"); 
      print(gamerules); 
      fav=int(input("Enter your choice : ")); 
      match fav : 
        case 1 : 
         print(gamerules);

     
       

         time.sleep(3);  

  case 2 : 
     print(gamerules);
     time.sleep(3); 


  case 3 : 
     print(gamerules);
     time.sleep(3); 


  case 4 :
     print("Exiting...."); 
     time.sleep(3); 
     break; 
  case _ : 
   print("Pagal hai kya"); 
   time.sleep(3);  
     









 

