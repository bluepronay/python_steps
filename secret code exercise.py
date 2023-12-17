#secret code
choice=0; 
ch='a'
while(choice!=3):
 print("\t1.Encoding\n\t2.Decoding\n3.Exit..."); 
 choice=int(input("Enter your choice : ")); 
 match(choice): 
  case 1 : 
   
   string=input("Enter the string : "); 
   string=list(string); 
   string.append(string[0]); 
   string[0]='a'
   for i in range(1,3):
    string.insert(i,ch); 
   for i in range(3):
    string.append(ch); 
#    string=(str)(string); 
   string=''.join(string)
   print(string); 
  case 2 : 
   string=input("Enter the string : "); 
   string=list(string); 
   string[2]=string[-4];
   string=''.join(string);
   print(string[2:-4]); 
   
   


  case _ : print("bye..."); 
    
   