# Graphic Interface Subprogram
#Declare import libraries
import tkinter
import customtkinter
import sys
import Functions

#Set import from libraries
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from Functions import *
from .ui_Interface import *

#Define variables to libraries
wx_tk=tkinter
wx_ctk=customtkinter

def showMsg():
    messagebox.showinfo('Message', 'You clicked the Submit button!')
#Create buttons and set window based on string array
def button_wxTk(my_button,Tk):
    # set title window
    Tk.title("Tkinter Window")
    #variables
    m=50
    n=20
    #set values dimensions
    wxheight = int(len(my_button)/2 * m) #height
    wxheight+=m
    wxwidth = wxheight + n#width
    #set dimension window
    Tk.geometry(str(wxwidth) + "x" + str(wxheight))
    # set minimum dimensions based on string array and functions
    Tk.minsize(wxwidth, wxheight)
    # set maximum dimensions based on screen computer
    Tk.maxsize(Tk.winfo_screenwidth(), Tk.winfo_screenheight())
    # Create buttons
    k = 0
    for i in range(len(my_button)):
        if i % 2 == 0:
            wxbtn = wx_tk.Button(Tk,
                                 text=my_button[i],
                                 command=my_button[i + 1])
            wxbtn.place(x=n, y=n + (m * k))
            k += 1

#Create buttons and set window based on string array
def button_wxCTk(my_button,CTk):

    # set title window
    CTk.title("CustomTkinter Window")

    # variables
    m=50
    n=20

    # set values dimensions
    wxheight = (len(my_button) + 1) * (m / 2)  # height
    wxheight += m
    wxwidth = wxheight + n  # width
    # set dimension window
    CTk.geometry(str(wxwidth) + "x" + str(wxheight))
    # set minimum dimensions based on string array and functions
    CTk.minsize(wxwidth, wxheight)

    # set maximum dimensions based on screen computer
    CTk.maxsize(CTk.winfo_screenwidth(), CTk.winfo_screenheight())
    #array of functions

    #Create buttons
    k=0
    for i in range(len(my_button)):
        if i%2==0:
            wxbtn = wx_ctk.CTkButton(CTk,
                                     text=my_button[i],
                                     command=my_button[i+1])
            wxbtn.place(x=n, y=n+(m*k))
            k+=1


#Another Test code
def geometry_wxTK(Tk):
#set dimensions based on screen computer
    # set Height x Width
    x = str(Tk.winfo_screenwidth())
    y = str(Tk.winfo_screenheight())
    return x + "x" + y
def size_Tk(Tk):#size on screen
    Tk.maxsize(Tk.winfo_screenwidth(), Tk.winfo_screenheight())

def dynamic_wxTK():
    print("Dynamic Tkinter Window")
    #in development
def dynamic_wxCTK():
    print("Dynamic CustomTkinter Window")
    #in development
def btn_Exit_Tk(Tk):
    print("Button Exit Tkinter")
    def Close():
        Tk.destroy()
    # Button for closing
    btn_exit_tk = Button(Tk, text="Exit", command=Close)
    btn_exit_tk.place(x=20, y=300)
def btn_Exit_CTk(CTk):
    print("Button Exit Custom Tkinter")

    def Close2():
        CTk.destroy()

    # Button for closing
    btn_exit_ctk = CTkButton(CTk, text="Exit", command=Close2)
    btn_exit_ctk.place(x=20,y=220)
def create_icon():
    print("Creating Icon")