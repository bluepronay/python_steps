#lists in python
#can contain various data types
#jump is present in lists
#comprehension
person=["Proni","Bhoumick",'M',19,True];
print(person);
print(type(person));       #list ki class hai
marks=[2,5,11,25];    #declaration
print(marks);         #aise print kar skte hai
print(marks[:]);         #aise v pura print kar skte hai
print(marks[0:len(marks)]);   #aise v pura print kr skte hai
print(marks[1:]);            #1st index se print kr skte hai
print(marks[-3:-1]);            #negative indexing v kaam krti hai
#same as string 

#to find a element/s in a list or a string
i=int(input("enter the no to find"));
if i in marks :
    print("yes,it is present");
else:
    print("not present");

s="Proni"

if 'on' in s :   #string mai v hai
    print("yeah");
else : 
    print("no way")

marks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];
print(marks[0:15:3]);         #the third is for the jump 

#if index starts from 5 to end 
#marks=[6,7,8,9,10,11,12,13,14,15,16]  ans=6,10,14
print(marks[5:len(marks):4]);
print(s[0:len(s):2]);             #strings mai v hai

#list comprehension

lst=[i*i for i in range(10)]      #for loop lagakar v value store kara skte hai,yha pe square store kar rha hai
print(lst)

even=[i for i in range(100) if(i%2==0)];         #for loop k andar condition v laga diya ab to even ka
print(even)                  #note yha pe ham colon nhi laga dete ,for k baad

# colours=[]
# size=int(input("Enter the size : "));
# for i in range(size):
#     k=int(input());
#     colours[i]=k;
# print(colours)