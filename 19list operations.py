# list operations
#list does change 
#1.append(val)

lst=[2,3,4,57,87,-8,45,0,3,2,2,8];
print(len(lst));
lst.append(-3);        #last mai jod dega
print(lst);

# print(lst.sort());   ye none dega
lst.sort(); 
print(lst);  #sort kar dega

lst=[2,3,4,57,87,-8,45,0,3,2,2,8];
print(lst);
lst.sort(reverse=True);
print(lst);        #reverse(sorted) mai print kar k dega;

lst=[2,3,4,57,87,-8,45,0,3,2,2,8];
lst.reverse();     #reverse mai print kar dega
print(lst); 

lst=[2,3,4,57,87,-8,45,0,3,2,2,8];
print(lst.index(2));         #ya to value ko store karao ya fir print karao
# print(lst.index(100))         ye index ki tarah hai string ki value hona hi chahiye

print(lst.count(2));          #count karega
print(lst.count(100));          

#####Important seekh#######
m=lst;    #m ko lst de diya
m[0]=9;
print(m)
print(lst)      #m hi print hoga
'''
this happened because m ab lst ka ek reference ban chuka hai 
which means any change in m will bring change to lst it is not like string
to avoid this we use copy function

'''
lst=[2,3,4,57,87,-8,45,0,3,2,2,8];
m=lst.copy();
m[0]=-2;
print(m); 
print(lst); #ab koi change nhi aayega

lst.insert(3,"Harry");     #index pe insert karne k liye lst.insert(index,val)
print(lst);

m=[45,50,76]; 
lst.extend(m);            #lst mai m jud jayega a kind of concatenation
print(lst);
print(m);
lst=[2,3,4,57,87,-8,45,0,3,2,2,8];
k=lst+m;
print(k)             #dono ko ek mai alag list mai jod dega
