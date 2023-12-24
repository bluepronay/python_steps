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
 
choosest='''
1. Snake
2. Water 
3. Gun
'''
while True : 
  print(well.center(80,'*')); 
  






