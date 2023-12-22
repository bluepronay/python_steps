#for and while loops with else 

i=1; 
for j in range(0,8):
    print(j); 
else : 
    print("No i ");     #jab nikal condition satisfy nhi hoga tab hoga

while(i<8):
    print(i); 
    i=i+1; 
else:             
    print("not i"); 

#question else execute hoga ya nhi

for k in range(3,10,2):
    if(k==7):
        print("k is 7 now exit from the loop"); 
        break;               #pure loop se hi bahar nikal rha hai that's why else execute nhi hoga last par
    print(k); 
else : 
    print("successfully completed the loop"); 