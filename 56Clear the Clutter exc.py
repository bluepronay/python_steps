'''
isme ham jis folder mai sare files ko rkh rhe hai , uss folder mai kisi ek particular type ki file ko pakad na hai
for example maine aise hi boht sare file bana diye yes.png,no.png,haa.png,nahi.png,good.png
aise kar k 
iss present directory mai abhi boht sari python files hai 
along with that boht sari txt files v hai jo kaam ki hai
so mai unme kuch changes nhi kar rha 
but mai kuch png files aise hi banakar , unhe ek baar mai hi rename karne ka try karunga
such as 1.png,2.png,3.png aise karke 

ISE HAM CLEAR THE CLUTTER BOLENGE....
ISKE LIYE OS MODULE CHAHIYE, USKA RENAME FUNCTION,listdir function un sabhi files ki list jo iss folder mai hai
uske baad ham sorting kar rhe hai unn files ki jinka naam .png se khatam ho rha hai
unhe ek list mai rkha 
and then uss list k har element mai hamne rename function chala diya 
iske baad vo sari files 1.png,2.png aise save ho chuki hogi 

NOTE : : : 
SO ISS KO CHALATE TIME PLS 10, 11 NAYE FILE BANA LE .png karke kisi v naam se 
varna yeh kaam nhi karega




'''

import os; 

def renamefile(oldname,newname):
    os.rename(oldname,newname); 



listfile=os.listdir()
# print(listfile)        agar mujhe sari files dekhni hai 
pngfiles=[file for file in listfile if file.endswith(".png")]; 
# print(pngfiles);        agar mujhe sari specific files dekhni hai
j=1; 
print("The CURRENT PNG FILES ARE : "); 
for i in pngfiles:
    print(i)
for i in pngfiles :    #ek file uthaya
    oldname=i; 
    newname=str(j)+'.png';     #newname mai pehle no joda then .png joda 
    renamefile(oldname,newname);   #oldname and newname ko argument ki tarah bhej diya
    j+=1; 
 
listfile=os.listdir()
pngfiles=[file for file in listfile if file.endswith(".png")];
print("AFTER RENAMING ALL THE FILES :"); 
for i in pngfiles :
    print(i); 
 
    
