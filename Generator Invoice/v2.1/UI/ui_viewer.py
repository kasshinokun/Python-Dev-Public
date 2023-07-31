#Code developed by Dev Prakash Sharma
#It's only example to learn 
#https://www.tutorialspoint.com/pdf-viewer-for-python-tkinter

#Import the required Libraries
import PyPDF2
from tkinter import *
from tkinter import filedialog

#Creating function 
def pdf_viewer():
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
#call function 
#pdf_viewer()
