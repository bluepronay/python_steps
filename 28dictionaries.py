# dictionaries in python
'''there are two parts here one is key and the other is value 
we can access the values using the keys


'''
dic={"Name":"Pronay","Branch":"AI",33:97};          #declaration
print(type(dic)); 
print(dic["Name"]);       #it will give pronay
#  print(dic["Pronay"]); this is wrong 
print(dic[33]);             #it will show 97
print(dic.get('Name')); #it will also show pronay but the basic difference is that it doesnot show errors 
#if anything is wrong then it will give none
print(dic.get('name'))         #it will give none
print(dic.keys());           #it will give the name of the keys that is name,branch and 33
print(dic.values());        #it will give te values
print(dic)

for key in dic:
    print(key)             #all the keys

for key in dic:
    print(dic[key])           #now the values

for key,value in dic.items() :     #syntax for the printing
    print(f"The value {value} corresponds to the key {key}");      #f string used
