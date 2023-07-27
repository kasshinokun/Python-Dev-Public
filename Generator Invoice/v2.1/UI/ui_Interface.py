# Graphic Interface Subprogram
from customtkinter import *
from tkinter import *
from .ui_functions import *

#Create Windows:
def wxTk():  # WindowsForm on Tkinter
    print("Tkinter Window")
    wxWindow = Tk()
    list_Tk = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    button_wxTk(list_Tk, wxWindow)
    wxWindow.mainloop()
def wxCTk():  # WindowsForm on CTkinter
    print("CustomTkinter Window")
    wxWindow = CTk()
    list_CTk = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    button_wxCTk(list_CTk,wxWindow)
    wxWindow.mainloop()
def dynamic_wxCTK():
    print("Dynamic CustomTkinter Window")
    wxWindow = CTk()
    dynamic_wx(wxWindow)
    wxWindow.mainloop()