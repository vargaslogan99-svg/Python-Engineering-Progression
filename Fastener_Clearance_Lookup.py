import sys

# Global variables
M_size = 0
Fit_type = "No response"
Exit_enter = "Y"

# This is the function to save values to a txt file
def save_value(a, b, m_val):
    Name_part = input("Enter a description for the specific part or name what the screw is for: ")
    
    with open("Tolerance_Log.txt", "a") as file:
        file.write(f"  \n")
        file.write("        ==============================================================\n")
        file.write(f"        Description/name: {Name_part}\n")
        file.write(f"        The M size is M{m_val}\n")
        file.write(f"        The hole type is {a} and the hole size is {b}mm\n")
        file.write("        ==============================================================\n")
        file.write(f"  \n")

#disclaimer for users
print(" ")
print("FASTENER CLEARANCE HOLE CALCULATOR (FDM OPTIMIZED)")
print(" ")
print("NOTICE: This tool uses a linear approximation of the ")
print("ISO 273 standard, optimized for FDM 3D printing ")
print("tolerances. Values may deviate by up to 5% from official ")
print("machining charts. Do not use for precision metalwork.")
print("This will create a file on your computer called 'Tolerance_Log.txt' ")
print("in your root folder if you are using an IDE ")
print("Use at your own discretion")
print(" ")

# User input and math calculation for the 5% deviation from the official values
while Exit_enter.upper() == "Y":
    Exit_enter = input("If you want to exit this program type 'n', if you are getting " \
    "your first value or need more type 'Y': ")
    
    if Exit_enter.upper() == "Y":
        user_response = "n"
        
        while user_response.lower() == "n":
            M_size_input = input("What size screw are you looking to use for this project(in mm): ")
            Fit_type = input("What fit are you aiming for? True, Tight, Hole, or Loose: ").title()
            print(f"Fit Type: {Fit_type}")
            print(f"M Size: {M_size_input}")
            user_response = input("Is the information above correct? [Y/n] ")
            if user_response.upper() == "Y":
                if Fit_type in ["True", "Tight", "Hole", "Loose"]:
                    try:
                        M_size = float(M_size_input)
                        if Fit_type == "True":
                            true_val = round(M_size * 1.05, 2)
                            print("Since you only want a hole as big as the " \
                            "screw, you should get a ", true_val, "mm sized screw.")
                            save_value(Fit_type, true_val, M_size)
                        elif Fit_type == "Tight":
                            Tight = round(M_size * 1.1, 2)
                            print("Since you want the screw to have a bit of bite" \
                            " on the wall. We will go with a hole size of ", Tight, "mm")
                            save_value(Fit_type, Tight, M_size)
                        elif Fit_type == "Hole":
                            Hole = round(M_size * 1.15, 2)
                            print("Since you want the hole to have the screw slide" \
                            " right through we will make the hole size ", Hole,  "mm")
                            save_value(Fit_type, Hole, M_size)
                        elif Fit_type == "Loose":
                            Loose = round(M_size * 1.20, 2)
                            print("You want this hole to be loose, allowing for" \
                            " your screw to slide in and out extremely easily. Here is your" \
                            " hole size: ",Loose, "mm")
                            save_value(Fit_type, Loose, M_size)
                    except ValueError:
                        print("[ERROR] Invalid input. Please enter just the number"
                        " (e.g., '3'). Try again.")
                        user_response = "n" # Force loop to repeat
                else:
                    print("[Error] Invalid fit type. Please check your spelling and try again.")
                    user_response = "n" # Force loop to repeat
            else:
                user_response = "n"
                
    elif Exit_enter.lower() == "n":
        print("Have a good day :)")
        sys.exit()
    else:
        print("Invalid input. Please enter 'Y' or 'n'.")
        Exit_enter = "Y" # Reset to keep the outer loop going