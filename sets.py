#sets in python
#if we don't want repeated items in our set then we use sets,{} is used here
#empty set's class is dictionary , the operations which we used to do in maths , we can do in here also
#the output of sets is not fixed , we can put same items but only once will be printed that's also in any order


b=[23,54]    #a list for experiment
s={2,9.4,54,3,5,1,3,2,7,2,44,2};     #it is printing in sorted order 
print(s);
a={"Harry","Potter","done",2,4,3,6.2,1.5,"done"};
print(a)
# a[0]="done"
# print(a[0])       sets does not support assignment
p={}
print(type(p));     #dictionary class
s=set(b);
print(type(s))        #set class
print(s)