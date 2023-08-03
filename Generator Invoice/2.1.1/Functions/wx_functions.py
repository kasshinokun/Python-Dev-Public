from tkinter import messagebox


def options_main(opt):
    if opt == 0:
        #before close message
        print("Goodbye")
        #return 1#Condition to break
    else:
        #Declaration to start procedures
        if opt == 1:
            #Call procedure
            print("Option 1")#function #1
        elif opt == 2:
            # Call procedure
            print("Option 2")  # function #2
        elif opt == 3:
            # Call procedure
            print("Option 3")  # function #3
        elif opt == 4:
            # Call procedure
            print("Option 4")  # function #4
        elif opt == 5:
            # Call procedure
            print("Option 5")  # function #5
        elif opt == 6:
            # Call procedure
            print("Option 6")  # function #6

        else:
            #If option isn't in the range
            print("\nInvalid Option.\n")
            print("\nRestarting Main...\n")
        #return 0

#options to graphic interface
def showMsg(val):
    messagebox.showinfo('Message', 'You clicked the Submit button '+val+' !')

def option_1():
    print("Option 1")
    showMsg("1")

def option_2():
    print("Option 2")
    showMsg("2")

def option_3():
    print("Option 3")
    showMsg("3")

def option_4():
    print("Option 4")
    showMsg("4")
