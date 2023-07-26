#Functions Subprogram
def options_main(opt):
    if opt == 0:
        #before close message
        print("Goodbye")
        return 1#Condition to break
    else:
        #Declaration to start procedures
        if opt == 1:
            #Call procedure
            print("1")#function #1
        elif opt == 2:
            # Call procedure
            print("2")  # function #2
        elif opt == 3:
            # Call procedure
            print("3")  # function #3
        elif opt == 4:
            # Call procedure
            print("4")  # function #4
        elif opt == 5:
            # Call procedure
            print("5")  # function #5
        elif opt == 6:
            # Call procedure
            print("6")  # function #6

        else:
            #If option isn't in the range
            print("\nInvalid Option.\n")
            print("\nRestarting Main...\n")
        return 0

