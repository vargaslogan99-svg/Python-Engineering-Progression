import sys

#Global variables(only the most common 99% use case screws)
M_size = 0
Fit_type = "No responce"
user_response = "n"

# disclaimer for users
print(" ")
print("  FASTENER CLEARANCE HOLE CALCULATOR (FDM OPTIMIZED)  ")
print(" ")
print("NOTICE: This tool uses a linear approximation of the ")
print("ISO 273 standard, optimized for FDM 3D printing ")
print("tolerances. Values may deviate by up to 5% from official ")
print("machining charts. Do not use for precision metalwork.")
print(" ")

# User input and math calculation for the 5% deviation from the official values
while user_response == "n":
    M_size = float(input("What size screw are you looking to use for this project(in mm): "))
    Fit_type = input("What fit are you aiming for? True, Tight, Hole, or Loose: ").title()
    user_response = input("Is the information above correct? [Y/n] ")
    if user_response == "Y" and Fit_type in ["True", "Tight", "Hole", "Loose"]:
        if Fit_type == "True":
            print("Since you only want a hole as big as the screw, " \
            "you should get a ",round(M_size * 1.05, 2),"mm sized screw.")
        elif Fit_type == "Tight":
            print("Since you want the screw to have a bit of bite on the wall" \
            "We will go with a hole size of ",round(M_size * 1.1, 2),"mm")
        elif Fit_type == "Hole":
            print("Since you want the hole to have the screw slide right through" \
            " we will make the hole size ", round(M_size * 1.15, 2),"mm")
        elif Fit_type == "Loose":
            print("You want this hole to be loose, allowing for your screw to " \
            "slide in and out extremely easily. Here is your hole size: ",round(M_size * 1.20, 2),"mm")
        else:
            print("Something went wrong try again.")
            sys.exit()
        

        


