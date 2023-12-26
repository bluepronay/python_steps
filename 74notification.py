from win10toast import ToastNotifier
import time
#how to make desktop notification 
toaster = ToastNotifier()

def notifications():
 toaster.show_toast("PAANI PEELE", "thak gye honge", duration=1); 

for i in range(3):
 notifications()
 time.sleep(3);    
