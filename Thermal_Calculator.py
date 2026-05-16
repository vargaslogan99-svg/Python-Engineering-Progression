
#global Var's
confirmation = "n"

# Dont use an (=), you must use a (:) because it represents a relationship vs a action
Material_dictionary = {
    "PLA": 0.0000835,
    "PLA_plus": 0.000068,
    "PETG": 0.000060,
    "ABS": 0.000100,
    "TPU": 0.000120,
    "Nylon": 0.00009,
    "CF_Fil": 0.000040
}

def save_value(material_name, b, c, d, e, f):
    Name_part = input("Enter a description for the specific part or name what this calculation is meant for: ")
    
    with open("Thermal_expansion_log.txt", "a") as file:
        file.write(f"  \n")
        file.write("        ==============================================================\n")
        file.write(f"        Description/name: {Name_part}\n")
        file.write(f"        The material is {material_name} and the expansion is {b}mm\n")
        file.write(f"        the length was {c} the projected final temperature was {d}, the starting temperature was {e}, and the type of expansion was {f}\n")
        file.write("        ==============================================================\n")
        file.write(f"  \n")

def calculate_expansion(material_name, original_length, final_temp, initial_temp, calculation_type = "linear"):
    if material_name in Material_dictionary:  

        Lookup = Material_dictionary[material_name]
        if calculation_type == "linear":
            expansion = (Lookup * original_length) * (final_temp - initial_temp)
        elif calculation_type == "area":
            expansion = (2 * Lookup * original_length) * (final_temp - initial_temp)
        elif calculation_type == "volume":
            expansion = (3 * Lookup * original_length) * (final_temp - initial_temp)
        else:
            return "Error: Invalid calculation type."
            
        return expansion
    else:
        return "Error: Material not found in our database."

print("==============================================================================")
print("this program is optimized for FDM components and materials")
print("This will create a file on your computer called 'Thermal_expansion_log.txt' ")
print("in your root folder if you are using an IDE ")
print("Use at your own discretion")
print("==============================================================================")


while True:
    material_choice = input("If you want to exit this program type 'n', if you are getting " \
    "your first value or need more type in the material you need checked: ")

    if material_choice == 'n':
        break

    if material_choice not in Material_dictionary:
        print("the material you tried to find was not in my dictionary.")
        continue

    try:
        
        while confirmation == 'n':
            material_choice in Material_dictionary
            print(" ")
            User_Stemp = float(input("what will be the starting temperature you plan to subject the" \
            " material to (enter value in celsius): "))
            print(" ")
            User_Ftemp = float(input("what will be the end temperature you plan to subject the" \
            " material to (enter value in celsius): "))
            print(" ")
            User_Msize = float(input("what is the original size (length in mm, area in mm², or volume in mm³): "))
            print(" ")
            User_Ctype = input("Do you want this for 'linear', 'area', or 'volume' expansion: ").lower()
            print(" ")
            print(User_Stemp,"degrees celsius",User_Ftemp,"degrees celsius",User_Msize,"mm", 
                  " type of expansion", User_Ctype)
            confirmation = input("are the input values above correct [Y/n] ")
    
    except ValueError:
        print("the input did not work try again(do not spell out the numbers ex. 1,2,3...)")
        continue
    print(" ")
    print("=====================")
    print(f"Given your values, the material will likely expand by: {calculate_expansion(material_choice,User_Msize,User_Ftemp,User_Stemp,User_Ctype)} units")
    print("=====================\n")
    print(" ")
    File_confirmation = input("would you like to save this to a text file? [Y/n]")
    if File_confirmation == 'Y':
        print("Saving your work... ")
        save_value(material_choice,calculate_expansion(material_choice,User_Msize,User_Ftemp,User_Stemp,User_Ctype),
                   User_Msize,User_Ftemp,User_Stemp,User_Ctype)
        print("Saved successfully.")
    
    confirmation = 'n'