# Import necessaries libraries
import tkinter.messagebox

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Specific import from libraries

# Specific import from folders
from release import functions

# Functions:
# Button Exit
def btn_close(CTkToplevel):#to close windows

    ctk.CTkButton(CTkToplevel,
                  text='Close',
                  command=CTkToplevel.destroy).pack(side='bottom', padx=20, pady=5, anchor='w')
#to setting size outside frame class
def g_frame(CTkFrame):#setting height and width frame 
    #CTkFrame.config(height=100, width=150, expand=True)#test code
     CTkFrame.config(height=100)#test code
     CTkFrame.config(width=150)#test code    
# Frame Class
class MainFrame(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container)
        #Set size
        #setting dimensions frame
        #self.config(height=100, width=150, expand=True)#test code
        #g_frame(self)#outside class 
        self.config(height=100)#test code
        self.config(width=150)#test code
        # show the frame on the container
        self.pack(side='top',  padx=20,pady=5, anchor='w')#left justified

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
#Initial function
def wx_start():#Initiate a program
    print("Starting")#Feedback
    wx = Wx_Parent()#Class on variable
    wx_t="Main"#title
    functions.default_CTk(wx,wx_t)#setting default size and title
    btn_open(wx)#to open child window
    btn_close(wx)#to close window
    frame=MainFrame(wx)
    wx.mainloop()#to stay on screen

wx_start()#Call start function
