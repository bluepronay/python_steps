import os;
import time;
amount=1000; 
q=0; 
kbc="!!!Kaun Banega Crorepati!!!"
print(kbc.center(100,'*'),"\n\n");
print("Some Rules Regarding the game....\nYou have 20 seconds to read them....\n1. Your Initial Amount:1000\n2.After every correct question,your amount will be doubled\n3. One Wrong Answer and you will come out with 5 Rupee\n4. If you want to exit in between,Enter '0'\n5. After the submission of every option u have to wait two second for the next question");
time.sleep(20);
os.system("cls");
que=["1. Who lost the final of World Cup of Cricket in 2011","2. Who won the World Cup of Football in 2018?","3. Who currently holds the record for the highest individual score in Test cricket?","4. Which year did India gain its independence from British rule?","5. Who is often referred to as the \"King Khan\" of Bollywood?","6. Which movie is considered the highest-grossing Bollywood film of all time?","7. Which iconic fort in Rajasthan is known as the \"Golden Fort\" due to its golden-hued walls?","8. Which country is known as the \"Land of the Rising Sun\"?","9. What is the tallest mountain in the world?","10. Base of Binary No System"]; 
options=[["1. England","2. India","3. Pakistan","4. Srilanka"],["1. France","2. Argentina","3. Portugal","4. Morroco"],["1. Virat Kohli","2. Rahul Dravid","3. Brian Lara","4. Adam Gilchrist"],["1. 1857","2. 1947","3. 1950","4. 1948"],["1. Shah Rukh Khan","2. Salman Khan","3. Saif Ali Khan","4. Amir Khan"],["1. Bahubali 2","2. Pathan","3. Dangal","4. Dil Wale Dulhaniya Le Jayenge"],["1. Mehrangarh Fort","2. Jaiselmer Fort","3. Chittorgarh Fort","4. Amer Fort"],["1. China","2. Indonesia","3. Japan","4. Malasiya"],["1. Guru Shikhar","2. Gauri Shankar","3. Mt. Everest","4. Choggori"],["1. 10","2. 2","3. 16","4. 8"]];
answer=[4,1,3,2,1,3,2,3,3,2]; 
for i in range(10):
    print(kbc.center(100,'*'),"\n\n");
    print("Your Current Balance : ",amount,"\n\n");
    print(que[i])
    for j in range(4):
     print(options[i][j])
    ans=int(input("Your Choice : "));
    if(ans==answer[i]):
       q=q+1; 
       amount=amount*2; 
       print("Correct Answer...\n Your Current Balance:",amount);
    elif(ans==0):
       print("Exiting with amount :",amount);
       break;
    else:
       print("Apne 5 rupe pakdo aur niklo...");
       amount=5;
       break;
    time.sleep(2.5)
    os.system("cls"); 
os.system("cls");
print(kbc.center(100,'*'),"\n\n");
print("Total Correct Answers :",q,"Out of 10\n");
print("Total Balance :",amount,"\n\n"); 
if(q==10):
   print("Congratulations,Winner.....\n\n");
elif(q>=7 and q<=9):
   print("Don't feel bad try for next time...\n\n");
elif(q>=4 and q<=6):
   print("Better Luck Next Time...\n\n"); 
else : 
   print("Kya hi bolu mai!!!\n\n");




