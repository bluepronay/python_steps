#OPERATOR OVERLOADING IN PYTHON
def sign(i): #just a function which can return sign 
    if(i>0):
        return "+"; 
    else : 
        return ""  #returned nothing
 
class vectors:
    def __init__(self,i,j,k):
        self.i=i;
        self.j=j; 
        self.k=k; 
    def __str__(self):  #this method is made so that i can do print(object)
        return(f'{self.i}i{sign(self.j)}{self.j}j{sign(self.k)}{self.k}k');   #don't care as much about this string, i just adjusted it according to vectors

    def __add__(self,other):   #OPERATOR OVERLOADING (DUNDER USED...) '+'
        return vectors(self.i+other.i,self.j+other.j,self.k+other.k); 
    
    def __sub__(self,other):   #OPERATOR OVERLOADING (DUNDER USED...)  '-'
        return vectors(self.i-other.i,self.j-other.j,self.k-other.k);



v1=vectors(8,7,5); 
print(v1); 
v2=vectors(4,3,9); 
print(v2); 
v3=vectors(3,-9,8); 
print(v3); 
v4=vectors(-7,-9,1); 
print(v4); 
v5=vectors(-7,-9,-6); 
print(v5); 
v6=v1+v2;  #OPERATOR OVERLOADING DONE, THE ADD METHOD RETURNED ANOTHER NEW VECTOR 
print(v6); 
v7=v3+v4;   #another operator overloading done
print(v7);
v8=v1-v2; 
print(v8);  