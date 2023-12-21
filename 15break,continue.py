#break and continue statements
#do while in python using break

for i in range(100) : 
    print(i);
    if(i==56):
        break;
for i in range(20) : 
    if(i%2==0):
        continue;             #even no ko chod do 
    print(i)


#do while loops in python using break statement

while True:                #to do a infinite loop  yha True hota hai
  i=int(input("Enter a no : "));
  if(i<0):
      break;
  elif(i%2==0):
      continue;
  else : 
      print(i);
print("loop closed"); 