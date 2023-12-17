#match case statement 
#it is similiar to switch case statement but the difference is that there is no necessary to use the break; statement here
#not only this it is also possible here to use if statement with the help of the default here
#here for default we do case_:

#let's make a match case for 

day=int(input("Enter the no of the day : "));
match day : 
    case 1 : 
        print("Monday");
    case 2 : 
        print("Tuesday");
    case 3 : 
        print("Wednesday");
    case 4 : 
        print("Thrusday");
    case 5 : 
        print("Friday");
    case _ if(day<8) :          #case _ if(condition) :
        print("Weekend");
    case _ if(day<11) : 
        print("Pagal hai kya!!");
    case _ :
        print("Invalid input");