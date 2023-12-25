#merging pdf files
#pip install pypdf2 
#pip install pycryptodome

#do this in the terminal of ur ide, then only u can do it,
#to run this program you have to add some pdf files in the folder you are running

#by the way i copied the code of merging from pypdf2 i just applied some logics here

import os; 
from PyPDF2 import PdfWriter

listpdfs=[files for files in os.listdir() if files.endswith('.pdf')]; 
for i in listpdfs:
    print(i)

merger = PdfWriter()

for pdf in listpdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()