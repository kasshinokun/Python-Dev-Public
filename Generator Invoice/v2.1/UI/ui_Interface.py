# Graphic Interface Subprogram
from customtkinter import *
from tkinter import *

#set dimensions based on screen computer
def geometry_wxCTK(CTk):  # set Height x Width
    x = str(CTk.winfo_screenwidth())
    y = str(CTk.winfo_screenheight())
    return x + "x" + y
def geometry_wxTK(Tk):  # set Height x Width
    x = str(Tk.winfo_screenwidth())
    y = str(Tk.winfo_screenheight())
    return x + "x" + y

#Create buttons based on string array
def button_wxCTk(my_button,CTk):
    k=0
    for button in my_button:
        wxbtn=Button(CTk,text=button).grid(row=k, column=0)
        k+=1
def button_wxTk(my_button,Tk):
    k = 0
    for button in my_button:
        wxbtn=Button(Tk,text=button).grid(row=k, column=0)
        k+=1

#Create Windows:
def wxTk():  # WindowsForm on Tkinter
    print("Tkinter Window")
    wxWindow = Tk()
    wxWindow.title("Tkinter Window")
    wxWindow.geometry(geometry_wxTK(wxWindow))
    list_Tk = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    button_wxTk(list_Tk, wxWindow)
    wxWindow.mainloop()
def wxCTk():  # WindowsForm on CTkinter
    print("CustomTkinter Window")
    wxWindow = CTk()
    wxWindow.title("CustomTkinter Window")
    wxWindow.geometry(geometry_wxCTK(wxWindow))
    list_CTk=['Option 1', 'Option 2', 'Option 3', 'Option 4']
    button_wxCTk(list_CTk,wxWindow)
    wxWindow.mainloop()