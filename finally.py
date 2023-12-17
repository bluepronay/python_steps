#finally keyword
#yeh hamesha execute hoga chahe error aaye ya fir naa aaye 

try : 
    i=int(input("Enter the index : ")); 
    a=[3,5,3,35,7]; 
    print(a[i]); 
except : 
    print("some error occured..."); 
finally : 
    print("i will always get executed ....."); 

#but the question is that isse farak kya pad gya ye to simple print daalne se v hojata
#ab socho agar ye kisi function mai hota tab agar ye return k baad hota to print ho jata 
#par agar simple print hota to kaam nhi hota therefore function k value return k baad v yeh to hoga hi

def final(b,a):
    try :
     print(b[a]); 
     return 1;
    except : 
       print("some error occured"); 
       return 0;
    finally : 
       print("i have executed....")


k=final(a,8); 
print(k)   #finally v print hua aur return statement wala v 