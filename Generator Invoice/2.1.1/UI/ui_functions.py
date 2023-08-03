import os
import sys
import PyPDF2
import customtkinter as ctk

import UI
from Functions import *
from tkinter import *


import tkinter as tk
from tkinter import ttk



#Create buttons and set window based on string array
def button_wxCTk(CTk,wxTitle,my_button):

    # set title window
    CTk.title(wxTitle)

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
    UI.max_CTk(CTk)
    #Create buttons
    #k=0 #variable to button in default setting size
    for i in range(len(my_button)):
        if i%2==0:
            wxbtn = ctk.CTkButton(CTk,
                                     text=my_button[i],
                                     height=20,
                                     command=my_button[i+1])
            #wxbtn.place(x=n, y=n+(m*k))#button in default setting size
            #Dynamic size button test
            wxbtn.pack(side='top',  padx=20,pady=5, anchor='w')#left justified
            #k+=1 #Increment to button in default setting size

    print(wxTitle+" on screen")
    CTk.resizable(True, True) #Dynamic size window ===> (true=(resizable height),true=(resizable width))

def teste_ux():#Test Code
    print("Interface Functions")
#class Wx_Frame():#Frame Class


class Wx(ctk.CTk):#Window Class

    def __init__(self):
        super().__init__()
        #set class based on array

        #print("Starting")
def start():#call main class based on variable
    app=Wx()#Instantiate the window
    #array to set buttons
    list_CTk = ['Generate PDF',
                UI.test_wx,
                'View PDF',
                lambda :options_main(2),
                'Open Frame',
                option_3,
                'Option 4',
                option_4]
    wx_t="Main CTk Window" #title of window
    button_wxCTk(app,wx_t,list_CTk)  # call function
    app.mainloop()
