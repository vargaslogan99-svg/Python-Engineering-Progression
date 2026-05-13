import sys

user_response = "n"
PLA = 0.012
PLA_Plus = 0.0175
PETG = 0.0175
ABS = 0.0225
TPU = 0.035
Nylon = 0.07
G_speed = 55
G_Layer = 0.2
G_Nozzel = 0.4

while user_response == 'n':
    Print_weight = float(input("How much dose the part you are trying to print weigh?(in grams): "))
    Filament_type = input(" what type of filament do you plan on using? PLA, PETG, PLA+, ABS, TPU, or Nylon? " \
    "type your answer exactly as the filament types have been spelled): ")
    Nozzle_size = float(input("what size nozzel are you using?(0.2mm, 0.4mm, 0.6mm, 0.8mm, etc.). If you dont know input '1010': "))
    Motion_spec = float(input("if you know your speed of your printer inpput in mm/s. If you dont know, input '1010'.: "))
    Layer_height = float(input("What layer height are you running? If you dont know put '1010'.: "))
    Volume = float(input("what Volume of the item you have created and are trying to print(in mm^3): "))
    print(Print_weight)
    print(Filament_type)
    print(Nozzle_size)
    print(Motion_spec)
    user_response = input("is are your inputs from above correct? ensure formating is proper and the " \
    "correct numbers have been input [Y/n]: ")
    if user_response == 'Y':
        if Filament_type == "PLA":
            Filament_type = PLA
        elif Filament_type == "PLA+":
            Filament_type = PLA_Plus
        elif Filament_type == "PETG":
            Filament_type = PETG
        elif Filament_type == "ABS":
            Filament_type = ABS
        elif Filament_type == "TPU":
            Filament_type = TPU
        elif Filament_type == "Nylon":
            Filament_type = Nylon
        else:
            print("there was an issue with your inputs, ensure you are not putting spaces in your responces. Please try again")
            sys.exit()
        print("Calculating your costs, and time...")
        print("your cost for this print will be $", (Filament_type * Print_weight))
        print("calculating print time...")
        if Motion_spec == 1010:
            Motion_spec = G_speed

        if Layer_height == 1010:
            Layer_height = G_Layer

        if Nozzle_size == 1010:
            Nozzle_size = G_Nozzel
        print("The print time for your moddel is ",(((Volume) /(Nozzle_size*Layer_height*Motion_spec))*1.2)/60," Minutes")