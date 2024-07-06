#game for truth and dare

import random

persons=['Pronay','Sachin','Sanidhya','Raju','Rahul']

dare=['Die instant','Cry harder','Propose her','Kill him','Dance in adivaasi style']

truth=['who\' your crush?','Money in your bank account','Do u support lgbtq?','Are u racist?','Your intrusive thought?']

while(len(persons)):
 a=random.choice(persons)
 b=random.choice(dare)
 c=random.choice(truth)
 d=int(input(f"{a} ,Enter 1 for truth or 2 for dare : ")); 
 if(d==1):
  print(f"{a} you have choosen truth and the question is {c}")
  persons.remove(a); 
  truth.remove(c); 
 else : 
  print(f"{a} You have choosen dare and the dare is {b}"); 
  persons.remove(a); 
  dare.remove(b); 


