#DIR(),__DICT__ AND HELP() FUNCTIONS IN PYTHON
#not so much useful, in this code btw

#1. USE OF DIR :- PYTHON MAI BOHT SARE CLASS BANE HUE HAI UN CLASSES K ANDAR KONSI ATTRIBUTES AND FUNCTIONS HAI ,
#UNHE PATA LAGANE K LIYE HAM ISKA USE KARTE HAI
list1=[2,3,4]; #ek list banayi
tuple1=(2,4); #ek tuple banayi
print(dir(list1)); 
methodslist=dir(list1); 
for i in methodslist:
    print(i)    #sabko dekho kitne sare function ho skte hai list mai
# print(dir(list))  ye v same hi deta
    
print("****TUPLE FUNCTIONS ARE ****")
for i in dir(tuple):
    print(i) #tuple functions dikh gye

print(list1.__add__);   #iska use yeh hua ki ab ham functions utha k unke bare mai dekh skte hai
print(list1.pop); 

print("\nDICT FUNCTIONS NOW"); 
#2. USE OF __DICT__
#let's define a class
class person:
    country="INDIA"; 
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print(f"Name : {self.name},Age : {self.age}, Country : {self.country}"); 

p1=person("Harry",35); 
p1.show(); 
print(p1.__dict__);  #isme sare instance variables aa jayenge dictionary k form mai , country nhi aayega
# ab isko lekar ham kahi pe store kar skte hai , as yeh dictionary k form mai aa rha hai

#RUN KARNE SE PEHLE Q DABA DENA AGAR PERSON KI HELP FUNCTION SE BAHAR NIKALNA HAI, AND AGAIN Q AGAR LIST SE BAHAR NIKALNA HAI TO 
#AGAR JYADA PADHNA HAI TO ENTER DABATE JAO
#3. HELP()
print(help(person));    #ye pura description batayega person class ki 
print(help(list))