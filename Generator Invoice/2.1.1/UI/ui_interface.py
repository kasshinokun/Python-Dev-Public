import UI
from Functions import *

def start():#call main class based on variable
    app=UI.Wx()#Instantiate the window
    #array to set buttons
    list_CTk = ['Option 1',
                lambda :options_main(1),
                'Option 2',
                lambda :options_main(2),
                'Option 3',
                lambda :options_main(3),
                'Option 4',
                lambda :options_main(4)]
    wx_t="Main CTk Window" #title of window
    UI.button_wxCTk(app,wx_t,list_CTk)  # call function
    UI.wx_Close(app)
    app.mainloop()
