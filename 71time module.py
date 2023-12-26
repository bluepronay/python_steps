#TIME MODULE IN PYTHON
import time

curernt=time.time(); #1979 se abhi tak kitna seconds ho chuke hai
print(curernt)

presentdate=time.strftime('%Y-%m-%d'); #aise karke date le skte hai
print(presentdate)

presentdate=time.strftime('%d/%m/%Y'); #agar iss format mai chahiye to
print(presentdate)

presenttime=time.strftime('%H:%M:%S'); #aise time nikal sakte hai
print(presenttime); 

for i in range(10):
    print(i); 
    time.sleep(1);  #use of time.sleep(seconds)  #aise output ko rok skte hai

#BAAKI ONLINE DOCUMENTATIONS PADHNA TIME MODULE K UPAR AND THEN FUTURE MAI JAISE NEED AAYE USS HISAAB SE CHAAPTE REHNA CODE
