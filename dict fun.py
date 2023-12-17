#dictionaries functions
ep={"Performance" : 33,"Job": 66,"Nice:" : 0}
print(ep)
ep1={"Performnce" : 36,"Jb": 98,"Nie:" : 1}
ep1.update(ep);    #same keys honge to pura ka pura copy ho jayega aur sab kuch nhi aayega that's why hame ab different keys lene honge

print(ep1); 
#baki sab same hai bas ek do farak hai jo yha pe hai
#pop
# a=ep1.pop; 
# print(a)   error aayega 
a=ep1.pop("Performance");  #pop mai key daalte hai tabhi kaam karega
print(a);      #is pe 33 aayega
print(ep1)

del ep1; 
# print(ep1)      error aa jayga
del ep["Job"]; 
print(ep); 