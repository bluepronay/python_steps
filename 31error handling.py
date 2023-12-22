#error handling in python
#normal code : 
a=input("Enter any no : "); 
# for i in range(1,11) : 
#     print(f"{int(a)} X {int(i)} = {int(a)*int(i)}");    #fstrings used

#but what if i enter a string while input

#in this case you have to do error handling cause in python if there is error then next lines are not executed
#if you want to execute the next lines than you have to do error handling 

try : 
    for i in range(1,11) : 
     print(f"{int(a)} X {int(i)} = {int(a)*int(i)}");

except : 
    print("error is occuring ")    #ye print hoga 



try : 
   for i in range(1,11):
      print(f"{int(a)}X{int(i)}={int(a)*int(i)}"); 
except Exception as e :                        #boht boht jaruri because yeh exception ka type batata hai
    print(e); 


array=[3,5,2]; 

try : 
   print(array[5]); 
except : 
   print("wrong"); 




#multiple exceptions
try : 
   print(array[5]); 
except ValueError:
   print("Value is wrong"); 
except SyntaxError:
   print("syntax error"); 
except IndexError:
   print("indexing error")      #isme yeh wala aayega

try : 
   print(a+3); 
except ValueError:
   print("Value is wrong"); 
except SyntaxError:
   print("syntax error"); 
except IndexError:
   print("indexing error"); 
except TypeError : 
   print("Its type error");  #yha ye aayega because concatenate ho pa rha


#therefor the thing is that we can use multiple exception here so that we can recognise which is the error
