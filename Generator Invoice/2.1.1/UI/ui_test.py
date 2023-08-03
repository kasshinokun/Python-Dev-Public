# Adaptation from:
# https://www.pythontutorial.net/tkinter/tkinter-toplevel/
import customtkinter
import os
import sys
import PyPDF2
import customtkinter as ctk
import tkinter as tk

from Functions import *
from UI import *
from tkinter import *
from tkinter import ttk


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


def btn_Exit(CTk):
    wxbtn = ctk.CTkButton(CTk, text='Close', command=option_1)
    # Dynamic size button test
    wxbtn.pack(side='bottom', padx=20, pady=5, anchor='w')  # left justified


class WxF(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # array to set buttons
        list_CTk = ['Option 1',
                    option_1,
                    'Option 2',
                    option_2,
                    'Option 3',
                    option_3,
                    'Option 4',
                    option_4]
        wx_t = "Child CTk Window"  # title of window
        button_wxCTk(self, wx_t, list_CTk)  # call function


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
                      command=lambda: identify(ctk.CTk)).pack(side='top', padx=20, pady=5, anchor='w')  # left justified
    def start_wx(self):
        wx_master = WxF(self)
        wx_master.grab_set()


def test_wx():
    wx = Main_wx()
    btn_Exit(wx)
    wx.mainloop()


def identify(obj):#identify type object
    # Need correction, show error
    if obj == ctk.CTk:
        print("It's a Window")
    elif obj == ctk.CTkFrame:
        print("It's a Frame")
    else:
        print("This is unknow for me")



