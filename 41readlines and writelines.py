#readlines() and writelines for file handling

'''
Readline is very necessary , as mostly when we read from a line then it contains 
many new lines due to which we have to use a for loop till the iterable object(line in this case becomes null)
this readline will take the character as string due to which we have to do typecasting if the information which 
is coming is int or float
'''
f=open('cupid.txt','r'); 
while True : 
    line=f.readline(); 
    print(line); 
    if not line :       #important to use break statement , otherwise everything will be ruined
        print("Song Ended...\n"); 
        break;
f.close(); 

#A VERY STRONG EXAMPLE FOR THE USE OF READLINE FUNCTIONS, PERSONALLY MY FAVOURITE

def percentage(m1,m2,m3,m4) :   #function to calculate percentage
    sum=m1+m2+m3+m4; 
    sum=sum/400; 
    return sum*100; 

f=open("Marks.txt",'r'); 
i=0;
while True : 
    
    i+=1; 
    line=f.readline();
    if not line : 
        print("Result Ended....");
        break; 
    for m in line : 
        m1=int(line.split(',')[0]);     #we have seen this in string operations, we have seperated the items of a string with the comma character
        m2=int(line.split(',')[1]);     #now these were in strings, therefore we typecasted them into int
        m3=int(line.split(',')[2]); 
        m4=int(line.split(',')[3]); 
    print(f"The marks of student {i} is : \nMaths : {m1}\nSST : {m2}\nEnglish : {m3}\nHindi : {m4}");
    print("The percentage is : ",percentage(m1,m2,m3,m4));    #called the percentage function
f.close(); 


#WRITELINE FUNCTION
f=open("writeline.txt",'w'); 
line=["34\n","44\n","55\n","66\n","77\n"];   #all the characters in the list should be in string format , and also you should be responsible for '\n'
f.writelines(line); 
f.close(); 

#if i want to use to write the content of a whole list using for loop 
marks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];
f=open("writeline2.txt","w"); 
for m in marks : 
     m=str(m)            #typecasted the integer into string so that they can enter in the file 
     f.write(m+"\t");       #using space after every entery
f.close(); 