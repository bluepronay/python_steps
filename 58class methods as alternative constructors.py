#CLASS METHODS AS ALTERNATIVE CONSTRUCTORS
'''
ham constructors ka basic use jante hai ki vo object k attributes ko values pakdane k kaam aate hai
but agar mai object ko declare karte time uske attributes ko sahi format mai na bheju to 
that's why hame dusre conditions k liye ready rehna chahiye for 
example yha do example diye hue honge
'''
class employee:
    def __init__(self,n,id):  #jo constructors ham generally banate hai
        self.name=n
        self.id=id;
    def show(self):
        print(f"Name : {self.name} and id is {self.id}"); 

e1=employee("Harry",44); #maine iss format mai data pakdaya , badhiya kaam kiya
e1.show(); 
#agar data iss format mai hota to
info2="Proni-33"; 
info3="Sani-22"; 
info4="Dhaniya-88"; 
#ab kaise,pakdaenge data ko, i know from string split

#AGAR STRING SPLITTING BHUL GYE TO YEH STRING KO EK PARTICULAR CHARACTER SE TODTA HAI BOHT SARI PARTS MAI AND THEN EK LIST K
#FORM MAI STORE KARTA HAI , THAT'S WHY MAINE INDEXING KAR RKHA HAI, MOREOVER SARE ELEMENTS STRING HI HONGE THAT'S WHY INTEGERS KO TYPECAST 
#KAR K BHEJO

e2=employee(info2.split('-')[0],int(info2.split('-')[1])); #STRING SPLITING YAAD NHI??STRING OPERATIONS MAI JAO
e3=employee(info3.split('-')[0],int(info3.split('-')[1])); 
e4=employee(info4.split('-')[0],int(info4.split('-')[1])); 
e2.show(); 
e3.show(); 
e4.show(); 

print("\n\nAnswers of 2nd Examples..."); 
#OK SO KAAM TO BAN GYA BUT DEKHO CODE KITNA VAHIYAD LAG RHA HAI, THAT'S WHY EK ALTERNATIVE CONSTRUCTOR BANANA CHAHIYE
#JO ISS FORMAT MAI AANE WALI INFORMATION KO BADAL SAKE SO THAT , MAIN CODE KA LINE KAM HO

#2ND EXAMPLE FOR A STUDENT

class student:
    def __init__(self,n,r):  #vahi constructor jo ham hamesha use karte hai
        self.name=n; 
        self.roll=r; 
    def show(self):
        print(f"Name : {self.name} and roll no is {self.roll}"); 
    
    @classmethod            #this is the lesson yeh constructor class method hai yeh string ko leta hai and then ek instance return karta hai aur u can say format ko change karke asli constructor ko call kar rha hai
    def altconstructor(self,info):
        return self(info.split('-')[0],int((info.split('-')[1])));          #maine ab ek instance hi return kara diya,string ko todke
    
st1=student("Proni",33);    #jaise simple banaya vaise hi
info1="Sani-87"
info2="Rani-43"; 
info3="Sparshi-98"; 
st2=student.altconstructor(info1); #aise call karte hai agar particular format mai nhi hai to , ye instance return kar rha hai
st3=student.altconstructor(info2); 
st4=student.altconstructor(info3); 
st1.show(); 
st2.show(); 
st3.show(); 
st4.show(); 



