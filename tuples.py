#tuples in python
#same as list but they don't change
#declaration
tup=(2,4,5); 
print(type(tup),tup);

#if you are just assigning one value than the python will say it is of class int 
tup1=(1); 
print(type(tup1));

#to ignore the class int you have to leave ',' there
# tup1=(1,);
# print(type(tup),tup);

print(tup[2]);
tup=(1,3,'2',"harry",'blue');  #any data type 
print(tup);
print(len(tup));

#tup[2]=45   it is wrong we can't assign values directly to the tuples through indexes

for i in tup :
    print(i); 

tup=(2,3,4,3,2,5,6,3,20,10,55,); 
for i in tup :
    if(i%2==0):
        print(i);

# tup=(for i in range(20) if(i%2!=0))  not possible
#negative indexes is there
print(tup[0:5]); 
print(tup[:5]); 
print(tup[0:len(tup)]); 
print(tup[-3:]); 
print(tup[-9:-3]); 
print(tup[2: :3]);   #jumping is there

