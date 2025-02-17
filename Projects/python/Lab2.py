# Program Name: Lab2.py (use the name the program is saved as)
# Course: IT1113/Section W01
# Student Name: Mason McCree
# KSU Email Address: mmccree5@students.kennesaw.edu
# Assignment Lab Number:2
# Due Date: xx/xx/20XX # Purpose: What does the program do (in a few sentences)?
# This program asks a user for their first and last name, the number of books they have purchased and then displays their name and total points.

def calculate_points(books):
    if books==0:
        return 0
    elif books == 1 or books == 2:
        return 5
    elif books == 3 or books == 4:
        return 10
    elif books == 5:
        return 15
    elif books == 6 or books == 7:
        return 20
    else: return 25



def display_info(users):
    for user in users:
        print(f"{user['name']} purchased {user['books']} book(s) and earned {user['points']} points.")

user = []

total =0

while True:
    
    name = input("What is your name? ")
    if name == "quit":
        break
    books = int(input("How many books did you purchase? "))

    points = calculate_points(books)      

    total += points

    user_info = {
        "name": name,
        "books": books,
        "points": points

        
    }

    user.append(user_info)

display_info(user)
    
print(f"Total points for the month: {total}")


    