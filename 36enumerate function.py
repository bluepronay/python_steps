#emumerate function in python
marks=[2,6,22,64,63,99,100,84,44,66,55]; 
index=0;
for i in marks:
    print(i); 
    if(index==6):
        print("Shabash beta 100 lane k liye!!!\n"); 
    index+=1; 

#itna bda code likhna pada index ko v initialise karna pada but enumerate ek aisa function hai jo hame 
#saath mai index ki value v deta hai
for index,mark in enumerate(marks):
    print(index,mark); 
    if(index==6):
        print("Shabash beta 100 lane k liye!!!");


#yeh decide v kar skta hai ki starting index kaha se start hona chahiye
for inde,mark in enumerate(marks,start=1):
    print(mark); 
    if(inde==6):
        print("Shabaash beta 100 lane k liye!!"); 
 