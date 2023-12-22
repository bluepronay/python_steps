# file input and output
  # f=open('test.txt','r');  it will show error as it is not created earlier done

#there for first we have to create a file name text.txt then we can read its content,
#there are two arguments, one is file name and the other is the mode in which we want to open
#THE DEFAULT MODE IS READ MODE ONLY
f=open('test.txt','r'); 
# print(f);  it is totally wrong
t=f.read(); 
print(t); 
f.close();   #closing the file is necessary

#for writing , we don't need to create a file previously , it will create a file by default..
f=open('test1.txt','w');   
f.write("Hii I am Proni,Good"); 
f.close(); 

f=open('test2.txt','a');   #for appending
f.write("\nnice"); 
f.close(); 


#there is one other mode also create mode , x it is used for just creating a file , but if the same file is already created then it will show error

#with function k use   hame close karne ki need nhi file ko , bas identention ka dhyan rkhna
with open('test.txt','r') as f : 
    data=f.read(); 
    print(data); 

  
