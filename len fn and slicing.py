#string operations and slicing
#postive and negative slicing 
#len function
#by default length of the string maanta hai
fruit="Orange"; 
print(fruit);    #will print fruit
print(len(fruit));    #len() function is used to find the length of the string 
print(fruit[0:6]);   #will print from including 0 to excluding 6 index   = orange
print(fruit[0:4]);    # oran  ayega
print(fruit[:6]);     #by default 0 maan lega= orange
print(fruit[1:]);    #by default 6 maan lega  = range
print(fruit[0:-2]);    #fruit[0:length-2]  maanega which means = oran
print(fruit[-2:6]);    #fruit[length-2:6] maanega = ge
print(fruit[4:2]);    #kuch nhi hoga
print(fruit[-4:-2]);    #length-4 and length-2 maanega which means [2:4] =an