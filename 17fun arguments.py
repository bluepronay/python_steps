#function arguments types
#4 types

#1 Default arguments : yha pe ham pehle se hi arguments ki value deke rkhte hai

def sum(a=2,b=7):
    print(a+b)

sum()          #agar by default call lagana hai to arguments dene ki jarurat nhi hai same as default constructors in c++
sum(4)          #yha pe a ko 4 maan lega and b to 7 hai hi
sum(4,9.9)

#2 keyword arguments : yha pe ham keyword ko specify kar k call karte hai

sum(b=8)         #hamne yha specify kiya hai ki b ko 8 mano 
sum(b=9,a=-4)       #agar keyword k saath call laga rhe then no need of order

#3 required arguments : yha pe ek ya dono ki hi value nhi dete default mai fir hame call karna padta hai unki value k saath

def diff(a,b=8):
    print(a-b)

diff(7)        #a ka argument dena hi padega
diff(8,6)      #b ko maan lega

#4 variable length arguments : yha pe no of variables fix nhi hai list ya tuples pass karte hai 

def pro(*num) : 
    print("Total No : ",len(num));    #no of arguments jaan sakte hai
    print(type(num));    #tuple type ka argument hai
    pro=1; 
    for i in num :          #fir se loop chal rha hai
        pro=pro*i; 
    print(pro)
        
def avg(*num) : 
    sum=0; 
    for i in num : 
        sum=sum+i; 
    return sum/len(num);         #return statement v use karte hai

a=int(input("Enter the no : "));
b=int(input("Enter the no : "));
c=int(input("Enter the no : "));
d=int(input("Enter the no : "));
e=int(input("Enter the no : "));

pro(a,b,c,d,e); 
avg=avg(a,b,c,d,e);
print("The average is ",avg);


