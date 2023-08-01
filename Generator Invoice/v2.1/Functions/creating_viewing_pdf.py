#In future, I will create my version(objective of this: add knowledge)

#Generate_PDF Code-base developed by:
#https://medium.com/@asttrodev/tutorial-gerando-pdf-simples-com-reportlab-e-python-6b67e3692bef

#Extract_PDF Code-base developed by Geeks for Geeks 
#https://

#View_PDF Code-base developed by Dev Prakash Sharma 
#https://www.tutorialspoint.com/pdf-viewer-for-python-tkinter 

#Import the required Libraries 
import PyPDF2 

#Importing canvas from reportlab library 
from reportlab.pdfgen import canvas

#Another imports
from tkinter import * 
from tkinter import filedialog 
  
#creating function  #1
def view_PDF(): 
    #Create an instance of tkinter frame 
    win= Tk() 
    #Set the Geometry 
    win.geometry("750x450") 
    #Create a Text Box 
    text= Text(win,width= 80,height=30) 
    text.pack(pady=20) 
    #Define a function to clear the text 
    def clear_text(): 
       text.delete(1.0, END) 
    #Define a function to open the pdf file 
    def open_pdf(): 
       file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*"))) 
       if file: 
          #Open the PDF File 
          pdf_file= PyPDF2.PdfFileReader(file) 
          #Select a Page to read 
          page= pdf_file.getPage(0) 
          #Open PDF file 
  
  
  
    #Define function to Quit the window 
    def quit_app(): 
       win.destroy() 
    #Create a Menu 
    my_menu= Menu(win) 
    win.config(menu=my_menu) 
    #Add dropdown to the Menus 
    file_menu=Menu(my_menu,tearoff=False) 
    my_menu.add_cascade(label="File",menu= file_menu) 
    file_menu.add_command(label="Open",command=open_pdf) 
    file_menu.add_command(label="Clear",command=clear_text) 
    file_menu.add_command(label="Quit",command=quit_app) 
    win.mainloop() 

#declaring function
def extract_PDF():
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

#declaring function 
def generate_PDF(list_Names):
    try:

#With canvas.Canvas(archive.pdf) 
#creating canvas object that will be generate pdf archive 
#with inserted name and place. 
#In example was stored the object on pdf variable;
        name_pdf = input('Please, insert PDF name: ')
        pdf = canvas.Canvas('{}.pdf'.format(name_pdf))

#The function drawString(y,x,text) 
#uses a Cartesian plane with X and Y axes in the pdf sheet
#(page on A4 is setted by width=595.27; height=841.89).
#So with setted positions y = 247 and x = 700 
#to center on screen, after each name,age in list_Names
#will write each starting on position 700 
#and reducing x every time 
#finish writing a line with the name and age;
        x = 720
        for name,age in list_Names.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(name,age))

#pdf.setTitle(title) will add title on pdf;
        pdf.setTitle(name_pdf)

#pdf.setFont(Font Name, size) will select font and size for items;
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Guests List')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Name and Age')

#pdf.Save() will save all modifications 
#on specified path of canvas.Canvas() object;
        pdf.save()
        print('{}.pdf successful created!'.format(name_pdf))
    except:
        print('Error on generate {}.pdf'.format(name_pdf))

#Creating called variable list_Names of dictionary type tipo inserting some values;
list_Names = {'Rafaela': '19', 'Jose': '15', 'Maria': '22','Eduardo':'24'}

#call function GeneratePDF(list_Names) passing variable list_Names as argument;
#generate_PDF(list_Names)#test code

#call function to extract from pdf
#extract_PDF()#test code

#call function to view pdf
#view_PDF()#test code
