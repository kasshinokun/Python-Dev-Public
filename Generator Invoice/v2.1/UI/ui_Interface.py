# Graphic Interface Subprogram
from customtkinter import *
from tkinter import *
from .ui_functions import *
from .ui_viewer import *
from .ui_test import *

#Create Windows:
def wxTk():  # WindowsForm on Tkinter
    print("Tkinter Window")
    wxWindow = Tk()
    #array of strings and functions
    list_Tk = ['Option 1',option_1, 'Option 2', option_2,'Option 3',option_3, 'Option 4', option_4]
    button_wxTk(list_Tk, wxWindow)
    btn_Exit_Tk(wxWindow)
    wxWindow.mainloop()
def wxCTk():  # WindowsForm on CTkinter
    print("CustomTkinter Window")
    wxWindow = CTk()
    # array of strings and functions
    list_CTk = ['PDF Viewer',pdf_viewer, 'Multi-Window', start_wx,'Option 3',option_3, 'Option 4', option_4]
    button_wxCTk(list_CTk,wxWindow)
    btn_Exit_CTk(wxWindow)
    wxWindow.mainloop()

