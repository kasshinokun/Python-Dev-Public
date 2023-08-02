import os
import sys
import PyPDF2
import customtkinter as ctk

from Functions import *
from tkinter import *


import tkinter as tk
from tkinter import ttk


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
    max_CTk(CTk)
    #Create buttons
    k=0
    for i in range(len(my_button)):
        if i%2==0:
            wxbtn = ctk.CTkButton(CTk,
                                     text=my_button[i],
                                     command=my_button[i+1])
            wxbtn.place(x=n, y=n+(m*k))
            k+=1



def teste_ux():#Test Code 
    print("Interface Functions")
def g_CTK(CTk):#to specific dimension
#set dimensions based on screen computer
    # set Height x Width
    CTk.geometry("400x200")
    #Set minimum and maximum dimensions
    CTk.minsize(CTk.winfo_width(),CTk.winfo_heigth())
    max_CTk(CTk)#Call function to set
def min_CTk(CTk):#max size on screen
    CTk.minsize(CTk.winfo_width(), CTk.winfo_height())
def max_CTk(CTk):#max size on screen
    CTk.maxsize(CTk.winfo_screenwidth(), CTk.winfo_screenheight())

#class wxF(ctk.CTkFrame):
class wx(ctk.CTk):#Main Class
    def __init__(self):
        super().__init__()
        #set class based on array
        list_CTk = ['Option 1',
                    option_1,
                    'Option 2',
                    option_2,
                    'Option 3',
                    option_3,
                    'Option 4',
                    option_4]

        button_wxCTk(list_CTk, self)#call function

        print("Window on screen")
def start():#call main class based on variable
    app=wx()
    app.mainloop()