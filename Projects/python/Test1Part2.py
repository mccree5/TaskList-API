#Program Name: Test1Part1.py (use the name the program is saved as)
# Course: IT1113/Section W01
# Student Name: Mason McCree
# KSU Email Address: mmccree5@students.kennesaw.edu
# Test Number:1
# Due Date: xx/xx/20XX # Purpose: What does the program do (in a few sentences)?
# This program asks a user to say two primary colors (red,blue yellow) and the prgroam is supposed to display the mix between the two colors and dispkat an error if ther enter the incorrect thing.

def mix_colors(color1, color2):
    primary_colors = ["red", "blue", "yellow"]
    
    if color1 not in primary_colors or color2 not in primary_colors:
        print("Error: Invalid input. Please enter only primary colors (red, blue, yellow).")
        return
    
    if color1 == color2:
        print("Error: Please enter two different primary colors to mix.")
        return
    
    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        print("Mixing red and blue results in purple!")
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        print("Mixing red and yellow results in orange!")
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        print("Mixing blue and yellow results in green!")
    else:
        print("Unexpected error occurred.")

while True:
    color1 = input("Enter the first primary color (or type 'quit' to exit): ").strip().lower()
    if color1 == "quit":
        break
    
    color2 = input("Enter the second primary color (or type 'quit' to exit): ").strip().lower()
    if color2 == "quit":
        break
    
    mix_colors(color1, color2)
