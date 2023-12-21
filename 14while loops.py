#while loops in python
#basic syntax is i=0
#while(condition):
 #statements....
#you can use else statement along with the while loop which will come when the condition of the while loop is false
a=int(input("Enter the no : "))
i=1;
while(i<=10):
    print(a,"*",i,"= ",a*i,sep="");         #space nhi diya
    i+=1; 
else : 
    print("Table printed upto 10 times");            #tab execute hoga jab cond false hoga