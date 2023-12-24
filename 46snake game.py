#SNAKE , WATER AND GUN GAME
import random; 
import os; 
import time;
main=[[0,1,-1],[-1,0,1],[1,-1,0]]; 
def msg(a,b):
  if(a==0):
    print("\nYour Choice : Snake"); 
  elif(a==1):
    print("\nYour Choice : Water"); 
  elif(a==2):
    print("\nYour Choice : Gun"); 
  if(b==0):
    print("\nComputer's Choice : Snake"); 
  elif(b==1):
    print("\nComputer's Choice : Water"); 
  elif(b==2):
    print("\nComputer's Choice : Gun");
# Generate a random integer between 1 and 10 (inclusive)
 
os.system("cls"); 
well="SNAKE,WATER AND GUN GAME";
rules='''
First of all you have options of three kind of matches

1. 3 MATCH MODE
2. 5 MATCH MODE
3. 7 MATCH MODE
4. Exit

You have to select any one of them...

If you win more than half matches then you win the game

Best of Luck..
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
game="3 MATCH MODE";
while True : 
  os.system("cls"); 
  print(well.center(80,'*')); 
  print(rules); 
  mode=int(input("Enter your favourite mode : ")); 
  match mode : 
    case 1 : 
     os.system("cls"); 
     print(well.center(80,'*'));
     print("\n"); 
     print(game.center(80,'*'));
     print("\n\t\t\tMUST READ RULES\n"); 
     print(gamerules); 
     ch=input("\nType any key to continue..."); 
     win=0; 
     mt=1; 
     total=3; 
     while(mt<=total): 
      os.system("cls"); 
      print(well.center(80,'*'));
      print("\n"); 
      print(game.center(80,'*')); 
      print("\n"); 
      print("Match No :- ",mt,"\t\t\t\t\t\tTotal Wins :- ",win); 
      print(choosest);
      i=int(input("Enter your choice : ")); 
      j=random.randint(1,3); 
      i=i-1; 
      j=j-1; 
      result=main[i][j]; 
      msg(i,j); 
      if(result==0):
        print("\nMATCH DRAWN....");
        ch=input("\nPress any key to continue...."); 
      elif(result==-1):
        print("\nMATCH LOST....");
        mt=mt+1; 
        ch=input("\nPress any key to continue...."); 
      else : 
        mt=mt+1; 
        win=win+1; 
        print("\nMATCH WON....");  
        ch=input("\nPress any key to continue....");
     os.system("cls"); 
     print(well.center(80,'*'),"\n"); 
     if(mt==total):
      print("\nThanks for playing...."); 
     if(win>=2):
       print("\nThe Scorecard is ",win,"-",total-win,"You have have a preety good luck....\nYOU WON CUTIE....."); 
     else:
       print("\nThe Scorecard is ",win,"-",total-win,"\n\nBETTER LUCK NEXT TIME\n\n");
     ch=input("\nPress any key to continue...."); 

    case 2 :
     game1="5 MATCH MODE";
     os.system("cls"); 
     print(well.center(80,'*'));
     print(game.center(80,'*'));
     print("\n\t\t\tMUST READ RULES\n"); 
     print(gamerules); 
     ch=input("\nType any key to continue..."); 
     win=0; 
     mt=1; 
     total=5; 
     while(mt<=total): 
      os.system("cls"); 
      print(well.center(80,'*'));
      print("\n"); 
      print(game1.center(80,'*')); 
      print("\n"); 
      print("Match No :- ",mt,"\t\t\t\t\t\tTotal Wins :- ",win); 
      print(choosest);
      i=int(input("Enter your choice : ")); 
      j=random.randint(1,3); 
      i=i-1; 
      j=j-1; 
      result=main[i][j]; 
      msg(i,j); 
      if(result==0):
        print("\nMATCH DRAWN....");
        ch=input("\nPress any key to continue...."); 
      elif(result==-1):
        print("\nMATCH LOST....");
        mt=mt+1; 
        ch=input("\nPress any key to continue...."); 
      else : 
        mt=mt+1; 
        win=win+1; 
        print("\nMATCH WON....");  
        ch=input("\nPress any key to continue....");
     os.system("cls"); 
     print(well.center(80,'*'),"\n"); 
     if(mt==total):
      print("\nThanks for playing...."); 
     if(win>=3):
       print("\nThe Scorecard is ",win,"-",total-win,"You have have a preety good luck....\nYOU WON CUTIE....."); 
     else:
       print("\nThe Scorecard is ",win,"-",total-win,"\n\nBETTER LUCK NEXT TIME\n\n");
     ch=input("\nPress any key to continue....");
      
      


    case 3 :
     game2="7 MATCH MODE"; 
     os.system("cls"); 
     print(well.center(80,'*'));
     print(game.center(80,'*'));
     print("\n\t\t\tMUST READ RULES\n"); 
     print(gamerules); 
     ch=input("\nType any key to continue..."); 
     win=0; 
     mt=1; 
     total=7; 
     while(mt<=total): 
      os.system("cls"); 
      print(well.center(80,'*'));
      print("\n"); 
      print(game2.center(80,'*')); 
      print("\n"); 
      print("Match No :- ",mt,"\t\t\t\t\t\tTotal Wins :- ",win); 
      print(choosest);
      i=int(input("Enter your choice : ")); 
      j=random.randint(1,3); 
      i=i-1; 
      j=j-1; 
      result=main[i][j]; 
      msg(i,j); 
      if(result==0):
        print("\nMATCH DRAWN....");
        ch=input("\nPress any key to continue...."); 
      elif(result==-1):
        print("\nMATCH LOST....");
        mt=mt+1; 
        ch=input("\nPress any key to continue...."); 
      else : 
        mt=mt+1; 
        win=win+1; 
        print("\nMATCH WON....");  
        ch=input("\nPress any key to continue....");
     os.system("cls"); 
     print(well.center(80,'*'),"\n"); 
     if(mt==total):
      print("\nThanks for playing...."); 
     if(win>=4):
       print("\nThe Scorecard is ",win,"-",total-win,"You have have a preety good luck....\nYOU WON CUTIE....."); 
     else:
       print("\nThe Scorecard is ",win,"-",total-win,"\n\nBETTER LUCK NEXT TIME\n\n");
     ch=input("\nPress any key to continue....");
    
    case 4 :
      print("Thanks for playing....")
      print("EXITING....");  
      break; 
      



  
  






