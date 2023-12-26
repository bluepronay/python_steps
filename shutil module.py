#shutil module in python

'''
The following are some of the most commonly used functions in the shutil module:

shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. 
If the destination location already exists, the original file will be overwritten.

shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. 
If the destination location already exists, the original directory will be merged with it.

shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. 
This function is equivalent to renaming a file in most cases.

shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. 
This function is similar to using the rm -rf command in a shell.


'''

import shutil
import os; 
# destination_folder = r'C:\Users\LENOVO\Downloads' 

# shutil.copy('done.py', r'C:\Users\LENOVO\Desktop\Downloads\done2.py') To check it works or not
# listfiles=os.listdir(destination_folder); 
# for file in listfiles:
#     print(file)

# shutil.copy('done.py','done5.py');  #agar hame isi folder mai copy karna hai to koi path ko nhi chipkana
# shutil.copy('done.py',r"\Users\LENOVO\Downloads\done1.py");   #it worked...., bahar kisi folder mai copy bhejna hai to path chipkao, second argument mai r"path"
# # shutil.copy()
# # shutil.copy(r"C:\Users\LENOVO\Desktop\pro programs\decimal to binary.cpp",'new.cpp')  #bahar se andar lana hai to 

# shutil.move('new.cpp',r"C:\Users\LENOVO\Desktop\pro programs\pythonseaaya.cpp"); #isse ham kisi file ko seedha bahar bhej skte hai

# shutil.copytree(r'C:\Users\LENOVO\Desktop\python_prog\huka',r'C:\Users\LENOVO\Desktop\pro programs\aaja')  #aise folder copy kar skte hai
# shutil.rmtree(r'C:\Users\LENOVO\Desktop\python_prog\huka')  aise directory hi uda skte hai
os.remove('done.py')
os.remove('done5.py')