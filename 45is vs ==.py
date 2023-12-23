#difference between '==' and 'is' operator
'''
both are comparison based operator 
the == compares the value actually, 
agar koi do variable equal hai to yeh true dega 
for example 3==3 true hai , similarly agar kisi list,tuple , dictionary k andar k elements
v same hai tab v true dega  
haa obviously 3 and "3" mai to false hi dega
'''
'''
but for is operator ye thoda case different hai 
yeh true tab dega jab ek hi object ki baat chal rhi hai 
python actually immutable objects janta hai , agar maine a=3 and b=3 kar rkha hai
to python a and b k liye alag sa memory allocate nhi karega 
bcoz ye janta hai ki yeh constant hai and inki value change nhi hogi 
that's why python bolega yeh same object ko point kar rhe hai
but in case of list which is mutable yeh false hi bolega 
bcoz elements chahe do lists ki same ho par list aage v change ho skti hai
that's why false bolega par tuple immutable hai to uss time true bolega 
'''

a=3; 
b=3; 

print(a==b);         
print(a is b);

c=[3,4,5]; 
d=[3,4,5]; 

print(c==d); 
print(c is d); 

e=(3,4,5); 
f=(3,4,5); 

print(e==f); 
print(e is f); 

g=3; 
h='3'; 

print(g==h); 
print(g is h);

i="Proni"; 
j="Proni"; 

print(i==j); 
print(i is j); 

k=None; 
l=None; 

print(k==l); 
print(k is l); 


