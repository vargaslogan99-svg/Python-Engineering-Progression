#function to convert MPa to PSI and vice versa
def pressure_menu():
    
    print("  ")
    User_choice = float(input("would you rather convert MPa to PSI (1) or PSI to MPa (2) [1/2]: "))
    if User_choice == 1:
        print(" ")
        MPa = float(input("what is your MPa count: "))
        print("doing the math...")
        print(f"at {MPa} MPa, there is {MPa * 145.0377} PSI")
        print(" ")
    elif User_choice == 2:
        print(" ")
        PSI = float(input("what is your PSI count: "))
        print("doing the math...")
        print(f"at {PSI} PSI, there is {PSI * 0.00689476} MPa")
        print(" ")
    else:
        print(" something went wrong try again")
        return "fail"


#function to convert in-lbs to N-m and vice versa
def torque_menu():
    print("  ")
    User_choice = float(input("would you rather convert N-m to in-lbs (1) or in-lbs to N-m (2) [1/2]: ")) 
    if User_choice == 1:
        print("  ")
        N_m = float(input("what is your N-m count: "))
        print("doing the math")
        print(f"at {N_m} N-m, there is {N_m *  8.8507457916} in-lbs ")
        print("  ")
    elif User_choice == 2:
        print("  ")
        in_lbs = float(input("what is your in-lbs count: "))
        print("doing the math")
        print(f"at {in_lbs} in-lbs, there is {in_lbs * 0.112985} N-m ")
        print("  ")
    else:
        print(" something went wrong try again")
        return "fail"
    

def temp_menu():
    print("   ")
    User_USchoice = (input("what units are you trying to convert from (Celsius/Kelvin/Fahrenheit): ")).lower()
    temp_1 = float(input(f"what is the number of {User_USchoice} you are trying to convert from: "))
    User_UFchoice = (input("what units are you trying to convert to (Celsius/Kelvin/Fahrenheit): ")).lower()
    if User_USchoice == User_UFchoice:
        print("bro you are trying to convert to the same unit")
    elif User_USchoice == "celsius" and User_UFchoice == "kelvin":
        print(" ")
        print(f"your conversion from {temp_1} {User_USchoice} to {User_UFchoice} results in {temp_1 + 273.15}")
        print(" ")
    elif User_USchoice == "celsius" and User_UFchoice == "fahrenheit":
        print(" ")
        print(f"your conversion from {temp_1} {User_USchoice} to {User_UFchoice} results in {(temp_1 * (9/5))+32}")
        print(" ")
    elif User_USchoice == "kelvin" and User_UFchoice == "celsius":
        print(" ")
        print(f"your conversion from {temp_1} {User_USchoice} to {User_UFchoice} results in {temp_1 - 273.15}")
        print(" ")
    elif User_USchoice == "kelvin" and User_UFchoice == "fahrenheit":
        print(" ")
        print(f"your conversion from {temp_1} {User_USchoice} to {User_UFchoice} results in {(temp_1 - 273.15) * (9/5)}")
        print(" ")
    elif User_USchoice == "fahrenheit" and User_UFchoice == "kelvin":
        print(" ")
        print(f"your conversion from {temp_1} {User_USchoice} to {User_UFchoice} results in {(temp_1 - 32) * (5/9) + 273.15}")
        print(" ")
    elif User_USchoice == "fahrenheit" and User_UFchoice == "celsius":
        print(" ")
        print(f"your conversion from {temp_1} {User_USchoice} to {User_UFchoice} results in {(temp_1 - 32) * (5/9)}")
        print(" ")
    else:
        print(" something went wrong try again")
        return "fail"
    

while True:
    print("====================================================")
    print("You can choose one of the options listed below:")
    print("    1. Pressure")
    print("    2. Torque")
    print("    3. Temperature")
    print("    4. Quit")
    print("====================================================")

    User_choice = float(input("which of the options above do you want [1/2/3/4]: "))
    try:
        if User_choice == 1:
            pressure_menu()
        elif User_choice == 2:
            torque_menu()
        elif User_choice == 3:
            temp_menu()
        elif User_choice == 4:
            print("thank you for choosing my calculator, have a good day.")
            break
        else:
            print("invalid input try again")
    except ValueError:
        print("there was an error with an input type (try only numbers ex. 1,2,3...)")
