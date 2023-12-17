#raising custom error
#ek baat smjho agr yha ye harry likhta to python khud bol deta ki error hai 
#but ham chahte hai ki agar ye range k bahar koi value de deta hai to program vahi band ho jaye
#bcoz uss value ko ham aage use kar rhe hai then it is necessary ki program vahi crash kar jaye....
a=int(input("Enter a value between 3 to 10 : ")); 
if(a<3 or a>10):
    raise ValueError("value is not nice...."); 
else : 
    print("nice...")

print("hello")   #agar error aaya to yeh execute nhi hoga