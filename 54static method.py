#STATIC METHOD
'''
there is no special use of static method in general case 
it is present in class only , but it does not take the self as the arguments
it can take variables as arguments also
we are just defining them in the class so that, they are attached to any one class
'''
class arithmatic:
    def __init__(self,n):
        self.num=n; 
    def addnum(self,n):
        self.num=n+self.num; 
    @staticmethod
    def add(a,b):
        return a+b; 


a=arithmatic(3) #i declared a object and now num is 3
a.addnum(4);        #i send 4 as argument to add
print(a.num);     #ans is 7
print(a.add(4,5));    #ans is 9
print(a.add(a.num,8));     #ans is 7+8=15
print(arithmatic.add(4,8));      #i can call static methods in this way also by taking their class name , also




 