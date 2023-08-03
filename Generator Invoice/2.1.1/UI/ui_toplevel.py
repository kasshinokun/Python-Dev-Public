#Import necessaries libraries 
import customtkinter as ctk
import tkinter as tk

#Specific import from libraries

#Specific import from folders

#Functions:
#Geometry and Size

#Buttons and Exit

#Frame Class

#Child Window Class 
class Wx_Child(ctk.CTkTopLevel):
   def __init__(parent):
     super.__init__():
     self.geometry("500x600")
#Parent Window Class
class Wx_Parent(ctk.CTk):
   def __init__(self):
      self.geometry("500x600")
def wx_start():
   print("Starting")
