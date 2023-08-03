# Adaptation from:
# https://www.pythontutorial.net/tkinter/tkinter-toplevel/

import os
import sys
import PyPDF2
import customtkinter as ctk
import tkinter as tk
from Functions import *
from tkinter import *
from tkinter import ttk

#In use
from UI import *

def g_CTK(CTk):  # to specific dimension
    # set dimensions based on screen computer
    # set Height x Width
    CTk.geometry("400x200")
    # Set minimum and maximum dimensions
    min_CTk(CTk)
    max_CTk(CTk)  # Call function to set


def min_CTk(CTk):  # max size on screen
    CTk.minsize(int(CTk.winfo_width()), int(CTk.winfo_height()))


def max_CTk(CTk):  # max size on screen
    CTk.maxsize(CTk.winfo_screenwidth(), CTk.winfo_screenheight())

def identify(obj):#identify type object
    # Need correction, show error
    if obj == ctk.CTk:
        print("It's a Window")
    elif obj == ctk.CTkFrame:
        print("It's a Frame")
    else:
        print("This is unknow for me")

def btn_Exit(CTk):
    wxbtn = ctk.CTkButton(CTk, text='Close',command=CTk.destroy)
    # Dynamic size button test
    wxbtn.pack(side='bottom', padx=20, pady=5, anchor='w')  # left justified


class WxF(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # array to set buttons
        list_CTk = ['Option 1',
                lambda :options_main(1),
                'Option 2',
                lambda :options_main(2),
                'Option 3',
                lambda :options_main(3),
                'Option 4',
                lambda :options_main(4)]
        self.title("Child CTk Window")  # title of window
        for i in range(len(list_CTk)):
            if i % 2 == 0:
                wxbtn = ctk.CTkButton(self,
                                      text=list_CTk[i],
                                      height=20,
                                      command=list_CTk[i + 1])
                # Dynamic size button test
                wxbtn.pack(side='top', padx=20, pady=5, anchor='w')  # left justified
        wxbtn2 = ctk.CTkButton(self, text='Return', command=self.destroy)
        # Dynamic size button test
        wxbtn2.pack(side='bottom', padx=20, pady=5, anchor='w')  # left justified


class Main_wx(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Parent CTk Window")
        g_CTK(self)
        # place a button on the root window
        ctk.CTkButton(self,
                      text='Open a window',
                      command=self.start_wx).pack(side='top', padx=20, pady=5, anchor='w')  # left justified
        ctk.CTkButton(self,
                      text='Test Type',
                      command=lambda: identify(self)).pack(side='top', padx=20, pady=5, anchor='w')  # left justified
    def start_wx(self):
        wx_master = WxF(self)
        wx_master.grab_set()
def test_wx():
    wx = Main_wx()
    #btn_Exit(wx) #Founded error
    wx.mainloop()
#test_wx() #test code
