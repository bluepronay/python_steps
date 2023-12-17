#string operations

#strings are immutable which means that when we do any changes inside the string they will not convert,they 
#will copied to other string and the operations will be on that temporary string 

#1.len()
a="Hello";
print(len(a));
#print(a.len());   it is wrong very important to mention it as aage k sare isi format mai hai
a="!!@Hiii I am Proni bhoumick!@!!! ";   #len=33
print(len(a));

#2.  str.upper()
print(a.upper());        #changes into upper
print(a);

#3. str.lower()
print(a.lower()); 


a="!!My name is Proni Bhoumick***!!"; 

#4. str.rstrip("character")
print(a.rstrip("!"));    #to remove a particular character only present at last of the string strip kar rhe hai
print(a.rstrip("*"));      #kaam nhi karega   as * present hi nhi hai last mai
#print(a.rstrip("!","*"));    only one argument at a time

#5. str.repace("string","string")
a="!!My name is Proni is Bhoumick***!!"; 
print(a.replace("is","apun"));   #is ko hatakar apun kar dega

#6. str.split(" ")     data type list mai bhar dega sabhi strings ko jo space se seperated hai,ya fir koi character v daal sakte hai jisko vo seperation ki tarah treat karega
print(a.split(" "));  #['!!My', 'name', 'is', 'Proni', 'is', 'Bhoumick***!!']   array ki tarah ho gya 
print(a.split("*"));   # * se seperate karega

#7. str.capitalize()   first letter ko capital karke baaki sabko small kardega
a="my Name IS PRONI";
print(a.capitalize());      #My name is proni

#8. str.center(integer)   jitna integer hoga utna aage aur peeche se jagah bachayega
print(a.center(50));
print(len(a.center(50)));         #50 add karke batayega little bit controversial
print(a.center(60,"*"));     # * ko lagayega space ki jagah

#9. str.count("string")            count kar k batayega kitni frequency hai
print(a.count("I"));   # ans=2 nhi hoga to 0 batayega

#10. str.endswith("string")      rstrip ki tarah hi last mai check karega ki string present hai ya nhi,double single se farak nhi padta
print(a.endswith('i'));        #false   ham chahe to 
print(a.endswith('I'));     #true   ham chahe to "NI"  v kar skte hai 

#11. str.find("string")               string ki index return kar dega agar present hoga to varna -1
print(a.find("is"));
print(a.find("IS"));

#12. str.index("string")                same as find function but to use this it is necssary that the string should be present
print(a.index("IS"));
#print(a.index("is"));                error dikha dega        

a="Proni12"
#13. str.isalnum()             alphanumeric hai ya nhi batayega true ya false karke
print(a.isalnum());              #agar number nhi ho to false de dega number hona v jaruri hai

#14. str.isalpha()                 only alphabets mai true dega
a="!!My name is Proni is Bhoumick***!!"; 
print(a.isalpha());
b="proniwt"
print(b.isalpha());

#15. str.islower()              lower case hai ya nhi
print(b.islower());
 
#16 str.isupper()                upper case hai ya nhi
print(a.isupper());
print((a.upper()).isupper());        # upper case mai convert kar k check kiya

#17. str.isprintable()               agar print hote time vo dikhta hai to like \n,\t  nhi dikhta
b="Proni\tBhoumick";
print(a.isprintable());
print(b.isprintable());

#18. str.isspace()                check karta hai ki sirf white space hai ya nhi
b="\t\t";
print(a.isspace());
print(b.isspace());          #sirf space hai that's why true

#19. str.title()              har word k pehle letter ko uppercase bana deta hai  like title of anything
a="my name is proni Bhoumick";
print(a.title());

#20. str.istitle()            check karta hai title format mai hai ya nhi
print((a.title()).istitle());      #title mai convert kar k check kiya that's why it is true

#21. str.startswith("string")            like ends with hota hai vaisa hi hai
print(a.startswith("my name"));

#22. str.swapcase()                lower ko upper kar dega aur upper ko lower case mai
print(a.swapcase()); 
