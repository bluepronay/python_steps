#importing time module(inbuilt) and performing the exercise

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))         #string mai aaya hai int mai convert karna padega
print(hour)
min=int(time.strftime('%M'))
print(min)
sec=int(time.strftime('%S'))
print(sec)

if(hour > 4):
      if(hour<20):  
        if(hour<18):
          if(hour<12):
           print("Good Morning...");
          elif(hour<16): 
              print("Good Afternoon");
          else :
              print("Good Evening");
elif(hour>4 and hour<24) :
    print("Good Night")
      
 