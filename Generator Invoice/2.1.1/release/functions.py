import customtkinter as ctk

# Geometry and Size:
#default resolution and name
def default_CTk(CTkToplevel,name):
    CTkToplevel.geometry("300x400")
    CTkToplevel.title(name)

#minimum resolution
def min_CTk(CTkToplevel):  # max size on screen
    CTkToplevel.minsize(int(CTkToplevel.winfo_width()), int(CTkToplevel.winfo_height()))
#maximum resolution
def max_CTk(CTkToplevel):  # max size on screen
    CTkToplevel.maxsize(CTkToplevel.winfo_screenwidth(), CTkToplevel.winfo_screenheight())

#Create buttons and set window based on string array
def btn_wxCTk(CTkToplevel,wxTitle,my_button):

    # set title window
    CTkToplevel.title(wxTitle)

    # variables
    m=50
    n=20

    # set values dimensions
    wxheight = (len(my_button) + 1) * (m / 2)  # height
    wxheight += m
    wxwidth = wxheight + n  # width
    # set dimension window
    CTkToplevel.geometry(str(wxwidth) + "x" + str(wxheight))
    # set minimum dimensions based on string array and functions
    CTkToplevel.minsize(wxwidth, wxheight)

    # set maximum dimensions based on screen computer
    max_CTk(CTkToplevel)
    #Create buttons
    #k=0 #variable to button in default setting size
    for i in range(len(my_button)):
        if i%2==0:
            ctk.CTkButton(CTkToplevel,
                                     text=my_button[i],
                                     height=20,
                                     command=my_button[i+1]).pack(side='top',  padx=20,pady=5, anchor='w')#left justified
            #k+=1 #Increment to button in default setting size

    print(wxTitle+" on screen")
    CTkToplevel.resizable(True, True) #Dynamic size window ===> (true=(resizable height),true=(resizable width))