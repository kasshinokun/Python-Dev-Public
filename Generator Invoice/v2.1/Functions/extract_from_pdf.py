#Developed by Geeks for Geeks 
#In future, I will create my version(objective of this: add knowledge)

#Importing canvas from reportlab library 
from reportlab.pdfgen import canvas

#extract from pdf
# importing required modules
import PyPDF2

def pdf_extractor():
   # creating a pdf file object
   pdfFileObj = open('example.pdf', 'rb')

   # creating a pdf reader object
   pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

   # printing number of pages in pdf file
   print(pdfReader.numPages)

   # creating a page object
   pageObj = pdfReader.getPage(0)

   # extracting text from page
   print(pageObj.extractText())

   # closing the pdf file object
   pdfFileObj.close()

#call function
pdf_extractor()
