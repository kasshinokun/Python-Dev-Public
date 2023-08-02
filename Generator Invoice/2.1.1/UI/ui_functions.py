import os as wx_os
import sys as wx_sys
import PyPDF2
import pygi
import customtkinter as ctk
import tkinter as tk

from gi.repository import Gtk as gtk
from Functions import *


def teste_ux():#Test Code 
    print("Interface Functions")

class wx_GTK():#using GTK
    #starting code function
    def __init__(self):

        #setting window
        window = gtk.Window()
        window.set_title("PDF Management")
        window.set_default_size(500, 300)
        window.set_position(gtk.WindowPosition.CENTER)
        window.connect('destroy', self.destroy)

        #setting button 
        wx_btn_1 = gtk.Button("Option #1")
        button.connect("clicked", self.button_clicked)
        window.add(wx_btn_1)#funtion inside class 
       
        wx_btn_2 = gtk.Button("Option #2")
        wx_btn_2.connect("clicked", self.outside_wx)
        wx_btn_2.add(wx_btn_2)#funtion outside clas

        #to close app(equals main.loop)
        window.show_all()

    #Adding functions inside class
    def button_clicked(self, window):
        print 'Inside test!'#print on screen 
   
    def destroy(self, window):
        gtk.main_quit()#to close app
        
#Add function outside class 
def outside_wx():
    print 'Outside test'
def main():# attributing class to function 
    app = wx_GTK()
    gtk.main()
def wx_start():# function to call class
    if __name__ == '__main__':
        main()#function
