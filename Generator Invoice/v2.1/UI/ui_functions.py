# Graphic Interface Subprogram
#Define and declare library 
import customtkinter as wx_ctk
import tkinter as wx_tk
import sys

#Set import from library 
from wx_ctk import *
from wx_tk import *


#Create buttons and set window based on string array
def button_wxTk(my_button,Tk):
    # set title window
    Tk.title("Tkinter Window")
    #variables
    k = 1
    m=50
    n=20
    #set values dimensions
    wxheight = (len(my_button) + k) * m#height
    wxwidth = wxheight + n#width
    #set dimension window
    Tk.geometry(str(wxheight) + "x" + str(wxheight+m))
    # set minimum dimensions based on string array
    Tk.minsize(wxwidth, wxheight)
    # set maximum dimensions based on screen computer
    Tk.maxsize(Tk.winfo_screenwidth(), Tk.winfo_screenheight())
    # Create buttons
    for button in my_button:
        wxbtn=wx_tk.Button(Tk,text=button).place(x=m, y=m*k)
        k+=1
#Create buttons and set window based on string array
def button_wxCTk(my_button,CTk):
    # set title window
    CTk.title("CustomTkinter Window")
    # variables
    k = 1
    m=50
    n=20
    # set values dimensions
    wxheight = (len(my_button) + k) * m# height
    wxwidth = wxheight+n# width
    # set dimension window
    CTk.geometry(str(wxwidth) + "x" + str(wxheight+m))
    # set minimum dimensions based on string array
    CTk.minsize(wxwidth, wxheight)
    # set maximum dimensions based on screen computer
    CTk.maxsize(CTk.winfo_screenwidth(), CTk.winfo_screenheight())
    #Create buttons
    for button in my_button:
        wxbtn=wx_ctk.CTkButton(CTk,text=button).place(x=m, y=m*k)
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
def dynamic_wx(CTk):
    #set grid column configure
    Grid.columnconfigure(CTk, index=0, weight=1)
    Grid.columnconfigure(CTk, index=1, weight=1)
    #set array
    my_buttons=["button 1","button 2","button 3","button 4"]
    # set title window
    CTk.title("Dynamic CustomTkinter Window")
    # variables
    k = 1
    m = 50
    n =30
    # set values dimensions
    wxheight = (len(my_buttons) + k) * m  # height
    wxwidth = wxheight + n  # width
    # set dimension window
    CTk.geometry(str(wxwidth) + "x" + str(wxheight + m))
    # set minimum dimensions based on string array
    CTk.minsize(wxwidth, wxheight)
    # set maximum dimensions based on screen computer
    CTk.maxsize(CTk.winfo_screenwidth(), CTk.winfo_screenheight())
    # Create buttons
    k=0

    for button in my_buttons:
        #column #1
        wxbtn = wx_ctk.CTkButton(CTk, text=button+" row "+str(k+1)+" column 1").grid(row=k, column=0, sticky="nsew")
        # set grid column configure
        Grid.rowconfigure(CTk, index=k, weight=1)

        # column #2
        wxbtn1 = wx_ctk.Button(CTk, text=button+" row "+str(k+1)+" column 2").grid(row=k, column=1, sticky="nsew")
        # set grid column configure
        Grid.rowconfigure(CTk, index=k, weight=1)
        k+=1
