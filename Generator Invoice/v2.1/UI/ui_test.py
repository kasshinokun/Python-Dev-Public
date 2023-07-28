import tkinter
import customtkinter

from tkinter import *
from customtkinter import *
#test class
class Parent():
      
    def show(self):
        print("Inside Parent")
          
class Child(Parent):
      
    def show(self):
          
        
        
        super().show()
        print("Inside Child")
def test_class_parent_child():          
    obj = Child()
    obj.show()
class FirstWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Settings Main Window
        self.title('First Window')
        self.configure(background='green')
        self.geometry('480x240')


class SecondWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Settings Main Window
        self.title('Second Window')
        self.configure(background='darkgray')
        self.geometry('480x240')


class ThirdWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Settings Main Window
        self.title('Third Window')
        self.configure(background='yellow')
        self.geometry('480x240')


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        #Setting Main Window
        self.master.title('Main Window')
        self.master.geometry('480x240')
        self.configure(borderwidth=4)
        self.configure(background='white')

        for name in ("button1", "button2", "button3"):
            self.button = Button(self, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Packaging Main Frame
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('1'):
            window = FirstWindow()
        if btn_name.endswith('2'):
            window = SecondWindow()
        if btn_name.endswith('3'):
            window = ThirdWindow()

        window.mainloop()


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop() 
#test_class_parent_child()# call test class 
