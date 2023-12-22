#seek() and tell() functions in python
#truncate() function also
#let me create a file named intro.txt we will read its content from that
#the content in this file is 
'''
Hii I am Proni, how are you??
fine nice to meet you 
see you again!!!
'''
with open('intro.txt','r') as f : 
    f.seek(20);       #it will move the current postion to 20 bytes in this file such as the space before 'are'
    data=f.read(15);    #it will print the next 15 bytes which is     are you??\nfine
    print(data); 
    print(f.tell());     #it will tell the current position which should be 36 now
    f.seek(4);      #fir se vahi se start ho gya
    print(f.tell());  #is baar 4 hi aayega as read nhi kiya abhi tak
    data=f.read(10); 
    print(f.tell(),data); #is baar f.tell 14 batayega 4+10 but in the case of new line ye one plus karke batata hai
    data=f.read(25);    #iss baar yeh new line ko v le lega that's why ab ye 14+25+1 = 40 batayega
    print(f.tell(),data); 

with open("Sample.txt",'w') as f :   #nyi file create kari iss naam se
    f.write("Hello,Proni!! How are you???");    #ye wala string bheja file k andar
    f.truncate(7);    #maine file k size ko limited kar diya hai 7 bytes tak which means 7 byte k baad koi v info ab andar nhi jayega

with open("Sample.txt","r") as f :     #ab file ko fir se open kiya read karne k liye
    data=f.read(); 
    print(data);    #hame puri info nhi milega

#agar truncate ka sahi use jan na hai to line no 24 ko comment karke dekhna
