
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

def save_value(material_name, b, c, d, e):
    Name_part = input("Enter a description for the specific part or name what this calculation is meant for: ")
    
    with open("Thermal_expansion_log.txt", "a") as file:
        file.write(f"  \n")
        file.write("        ==============================================================\n")
        file.write(f"        Description/name: {Name_part}\n")
        file.write(f"        The material is {material_name} and the expansion is {b}mm\n")
        file.write(f"        the length was {c} the projected final temperature was {d}, and starting temperature was {e}\n")
        file.write("        ==============================================================\n")
        file.write(f"  \n")

def calculate_expansion(material_name, original_length, final_temp, initial_temp):
    if material_name in Material_dictionary:  

        Lookup = Material_dictionary[material_name]
        expansion = (Lookup * original_length) * (final_temp - initial_temp)
        return expansion
    
    else:

        return "There was an error during the calculation process. The " \
        "material entered was not found in our database."

print("=====================================================================")
print("this program is optimized for FDM components and materials")
print("This will create a file on your computer called 'Thermal_expansion_log.txt' ")
print("in your root folder if you are using an IDE ")
print("Use at your own discretion")
print("=====================================================================")


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
            User_Stemp = float(input("what will be the starting temperature you plan to subject the" \
            " material to (enter value in celsius): "))
            User_Ftemp = float(input("what will be the end temperature you plan to subject the" \
            " material to (enter value in celsius): "))
            User_Msize = float(input("what is the length of the material you plan to use in its " \
            "starting temperature (in mm): "))
            print(User_Stemp,"degrees celsius",User_Ftemp,"degrees celsius",User_Msize,"mm")
            confirmation = input("are the input values above correct [Y/n] ")
    
    except ValueError:
        print("the input did not work try again(do not spell out the numbers ex. 1,2,3...)")
        continue
    print(" ")
    print("=====================")
    print("given the values from you, your material will likely expand",
          (calculate_expansion(material_choice,User_Msize,User_Ftemp,User_Stemp), "mm"))
    print("=====================")
    print(" ")
    File_confirmation = input("would you like to save this to a text file? [Y/n]")
    if File_confirmation == 'Y':
        print("Saving your work... ")
        save_value(material_choice,calculate_expansion(material_choice,User_Msize,User_Ftemp,User_Stemp),
                   User_Msize,User_Ftemp,User_Stemp)
    
    confirmation = 'n'


#dictionary test
#print("The material coefficent for TPU is: ",Material_dictionary["TPU"])