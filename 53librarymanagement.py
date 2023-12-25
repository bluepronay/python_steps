#library management system in python

class library : 
    def __init__(self,n):        #SABSE PEHLI BAAR MAI BOOKS KA NO MANG RHA HU , SAATH HI UNKE NAAM V MANG RHA HU
        self.nobooks=n; 
        self.books=[]
        for i in range(0,n):
            b=input(f"Enter the name of {i+1} book : ");   
            self.books.append(b);            #ISS LIST MAI MAINE JOD DIYA BOOKS KO
        
    def addbooks(self):
        book=input(f"Enter the name of {len(self.books)+1} book : ")           #BAAD  MAI KABHI BOOKS JODNA HUA TO
        self.books.append(book); 
        self.nobooks+=1; 
    def show_details(self):
        print("Total no of books available : ",self.nobooks); 
        print("Books are : ");                #DETAILS SHOW KAR DIYA
        for i in self.books:
            print(i); 



n=int(input("How many books you want to enter in the first : ")); 
lib1=library(n);  #object declare kiya
lib1.show_details(); 
lib1.addbooks();    #baad mai book add v kar skte hai
lib1.show_details();  

#lib2=library(4)   dusri library v bana skte hai, (objects) and uske andar alag books rkh skte hai
#this is just a simple example to show you the power of oops
    

        