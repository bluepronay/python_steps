#set methods in python
#same as set theory

#UPDATE    ye tuple aur dictionary mai v kaam kar skta hai
name={"Korbo","lorbo","jeetbo"}; 
name1={"jeetbo","re"}; 
print(name); 
print(name1); 
name.update(name1); 
print(name);    #update mai usi set mai change ho jayega
print(name1); 



#UNION
cities={"Jaipur","Bhopal","Jaiselmer","Kolkata"};
cities1={"Lahore","islamabad","alahabad","Kolkata"}; 
ci=cities.union(cities1); 
print(ci);    #union mai naya set aa jata hai kolkata ek hi baar aayega


#INTERSECTION_UPDATE usi mai update karega

name={"Korbo","lorbo","jeetbo"}; 

name1={"jeetbo","re"}; 
name1.intersection_update(name); 
print(name1); 
print(name);  #ye to union hi dega


#INTERSECTION     naye mai store kara dega dono sets ka intersection
song={"ae mere dil","gulabi aakhe"}; 
songs={"jab se dekha", "ae mere dil"}; 
songs1=song.intersection(songs); 
print(song);
print(songs);
print(songs1);      #naye set mai intersection stored hai

#SYMMETRIC_DIFFERENCE         jo dono mai common nhi hai vo dono karega naye set mai
hero={"SRK","salman","saif"}; 
heros={"varun","kartik","SRK"}; 
he=hero.symmetric_difference(heros); 
print(he); 

#SYMMETRIC_DIFFERENCE_UPDATE     usi set mai update karega
hero.symmetric_difference_update(he); 
print(hero); 

#difference and difference update 
#actually ye A-B karega samjah ja
hero={"SRK","salman","saif"}; 
heros={"varun","kartik","SRK"}; 
he=hero.difference(heros); 
print(he); 


#isdisjoint()  check karega koi v common hai ya nhi
hero={"SRK","salman","saif"}; 
heros={"varun","kartik","SRK"}; 
print(hero.isdisjoint(heros));

#issuperset(); check karega superset hai ya nahi
int1={1,3,6}; 
int2={3}; 
print(int1.issuperset(int2)); 
print(int2.issuperset(int1)); 

#issubset()          check karega subset hai ya nhi
print(int1.issubset(int2)); 
print(int2.issubset(int1)); 

#add(element)        ek particular element ko add karega
hero.add("Amitabh"); 
print(hero);

#update in different data structures
lst=[5.6]; 
print(type(lst)); 
hero.update(lst); 
print(hero);      #list ko v jod liya apne mai

#remove(element),discared(element)      ye kisi ek particular element ko delete karne k kaam aayega
#remove mai agar vo element present nhi ho to error aayega discard mai koi error nhi aata
hero.remove("Amitabh"); 
print(hero); 
# hero.remove("Amitabh");   error aa gya
hero.discard("salman"); 
print(hero); 
hero.discard("salman");   #koi error nhi aayega
print(hero); 

#pop()   last element ko remove kar dega koi variable assighn kara dena 
hero.add("Akshay")
popped=hero.pop(); 
print(popped); 
print(hero)

#del         pure set ko uda dega fir access nhi kar skte
del int1; 
# print(int1);   error dega

#clear() khali karega delete nhi karega
int2.clear()
print(int2) 

#to check if any element is present or not
int1={"done",True,"22"}; 
val=input(); 
if val in int1:
    print("present"); 
else : 
    print("not present"); 
