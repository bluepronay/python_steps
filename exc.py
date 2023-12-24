import os; 

listfile=os.listdir()
print(listfile)
for files in listfile :
    print(files)
    if(files endswith '.log'):
        print(files) 
