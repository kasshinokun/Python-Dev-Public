# Import necessaries libraries
import tkinter.messagebox

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Specific import from libraries
#from customtkinter import *
# Specific import from folders
from release import functions

# Functions:
# Button Exit
def btn_close(CTkToplevel):#to close windows

    ctk.CTkButton(CTkToplevel,
                  text='Close',
                  command=CTkToplevel.destroy).pack(side='bottom', padx=20, pady=5, anchor='w')
#to setting size outside object class
def p_wx(CTkToplevel):
    CTkToplevel.pack_configure(side='top',padx=20, pady=5, fill='both', anchor='w', expand=True)
#Frame Class
class Wx_Frame(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container)


# Child Window Class
class Wx_Child(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

#Call Child Window
def wx_w(CTkToplevel):
    window = Wx_Child(CTkToplevel)#class on variable
    #array of strings and functions
    list_CTk = ['Open Child Window',
                lambda: wx_w(window),
                'Option 2',
                lambda: print("option 2"),
                'Option 3',
                lambda: print("option 3"),
                'Option 4',
                lambda: print("option 4")]
    wxtitle = "Child"#title
    functions.btn_wxCTk(window, wxtitle, list_CTk)#Add buttons and set window
    btn_close(window)#to close window
    window.grab_set()#to change focus
# Parent Window Class
class Wx_Parent(ctk.CTk):
    def __init__(self):
        super().__init__()
#Button open
def btn_open(CTkToplevel):#to open windows
    ctk.CTkButton(CTkToplevel,
                  text='Open default child window',
                  command=lambda: wx_w(CTkToplevel)).pack(side='top', padx=20, pady=5, anchor='w')

#test frame with predefined functions
def wx_wx():#some details will added on future
    print("start a frame")
    #instanciate the objects:
    
    #setting frame
    
    #labels
    
    #entries
    
    #buttons
    
    #feedback on console(terminal/system prompt)

#Initial function
def wx_start():#Initiate a program
    print("Starting")#Feedback
    wx = Wx_Parent()#Class on variable
    wx_t="Main"#title
    functions.default_CTk(wx,wx_t)#setting default size and title
    btn_open(wx)#to open child window
    btn_close(wx)#to close window
    wx_frame = Wx_Frame(wx)
    #set dynamic size frame
    p_wx(wx_frame)

    wx.mainloop()#to stay on screen

wx_start()#Call start function
