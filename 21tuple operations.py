#operations in tuples
'''
we can't do direct operations in tuples like we used to do in lists
to do any operations first of all we have to convert that tuple into a new list 
then we should do the operations
after the operations we can again convert back the list into tuple 
so every operation can be done with the tuple but in a indirect way..
'''
name=("Proni",'sparshi','sani','sachin'); 
print(name[2]);
print(name);
if 'Proni' in name:      #it can be performed
    print("yes");
else:
    print("no");

#we can do concatenation in tuple to make a new tuple
sname=("bhoumick","sc","singhal");
fname=name+sname;
print(fname);
print(type(fname));

#index operation changes in tuple
inte=(1,2,3,3,5,6,7,2,9); 
n=len(inte);
print(inte.index(2));     #it will print the left most index of the element but i want to see for a particular range
print(inte.index(2,3,n));  #it will see for element in the range given 3 se leakar n tak dhund kaha milega
print(inte.index(7,4,n)); 

#now main thing to perform list operations in the tuples
name=(list)(name);      #convert into list
name.append("hetal");   #do the operation
print(name); 
name=(tuple)(name);     #again convert into tuple
print(name,type(name));