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
        print("Song Ended..."); 
        break;
f.close(); 