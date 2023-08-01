#Code developed by Dev Prakash Sharma
#It's only example to learn
#https://www.tutorialspoint.com/pdf-viewer-for-python-tkinter

#Import the required Libraries
import PyPDF2
import tkinter
import customtkinter

#Import required items from Libraries
from tkinter import *
from customtkinter import *
from tkinter import filedialog

#test class
class Parent():
      
    def show(self):
        print("Inside Parent")
          
class Child(Parent):
      
    def show(self):
          
        
        
        super().show()
        print("Inside Child")
def test_class_parent_child():          
    obj = Child()
    obj.show()
class FirstWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Settings Main Window
        self.title('First Window')
        self.configure(background='green')
        self.geometry('480x240')


class SecondWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Settings Main Window
        self.title('Second Window')
        self.configure(background='darkgray')
        self.geometry('480x240')


class ThirdWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Settings Main Window
        self.title('Third Window')
        self.configure(background='yellow')
        self.geometry('480x240')


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        #Setting Main Window
        self.master.title('Main Window')
        self.master.geometry('480x240')
        self.configure(borderwidth=4)
        self.configure(background='white')

        for name in ("button1", "button2", "button3"):
            self.button = Button(self, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Packaging Main Frame
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('1'):
            window = FirstWindow()
        if btn_name.endswith('2'):
            window = SecondWindow()
        if btn_name.endswith('3'):
            window = ThirdWindow()

        window.mainloop()

def start_wx():
    mainWindow = MainWindow()
    mainWindow.mainloop()

def start_wx_2():
    if __name__ == '__main__':
        mainWindow = MainWindow()
        mainWindow.mainloop()
#===================================================================================
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