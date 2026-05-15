#user warning
print("Use at your own discretion")

#global variables
File_name = input("What is the name of the .gcode file (ex. print.gcode):")
Filament_type = input("What filament did you use? ")
total_layers = "unknown"
print_time = "unknown"
grams_filament = "unknown"

print("Looking through the ", File_name, " for metadata.")

#parsing process
with open(File_name, "r", encoding= "utf-8") as file: 
    for line in file:
        if line.startswith(";"):
            # FIX 3: Attached .lower() to the line variable
            line_lower = line.lower()

            if "total layer number" in line_lower:
                pieces = line.split(":")
                total_layers = pieces[1].strip()
            
            elif "total estimated time" in line_lower:
                pieces = line.split(":")
                print_time = pieces[2].strip()
            
            elif "total filament weight" in line_lower:
                pieces = line.split(":")
                grams_filament = pieces[1].strip()

#user output/confirmation data is not corrupted when uploaded to new .csv file
print("=====================")
print("This came from a file named:", File_name )
print("There are", total_layers, "layer lines in this print.")
print("This print will take",print_time,"Minutes")
print("You will use", grams_filament,"grams of", Filament_type,".")
print("=====================")

# to create file -> add 'as csv_file:' to the end
with open("Print_history.csv", "a", encoding="utf-8") as csv_file:
    #didnt know this had to be in a f-string to make it a single text block. The more you know
    csv_file.write(f"{File_name},{print_time},{total_layers},{grams_filament},{Filament_type}\n")
    
print("Data successfully saved to Print_history.csv!")