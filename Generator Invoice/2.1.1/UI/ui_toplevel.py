#Import necessaries libraries 
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
      
#Specific import from libraries

#Specific import from folders

#Functions:
#Geometry and Size

#Buttons and Exit
def btn_open(ctk.CTk):
   CTkButton(ctk.CTk,
             text='Open a window',
                command=lambda: wx_open(ctk.CTk)).pack(side='top',padx=20,pady=5,anchor='w')
   
def wx_open(ctk.CTk):
        window = Wx_Child(CTk)
        window.grab_set()
def btn_close(ctk.CTkTopLevel):
   CTkButton(CTkTopLevel,
              text='Close',
              command=CTkTopLevel.destroy).pack(side='top',padx=20,pady=5,anchor='w')
#Frame Class

#Child Window Class 
class Wx_Child(ctk.CTkTopLevel):
   def __init__(self, parent):
        super().__init__(parent)
        self.geometry("500x600")
        self.title("")
#Parent Window Class
class Wx_Parent(ctk.CTk):
   def __init__(self):
      super().__init__()
      self.geometry("500x600")
      self.title("")
def wx_start():
   print("Starting")
   wx = Wx_Parent()
   wx.mainloop()
