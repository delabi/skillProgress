"""
This program helps boot camp participants track their progress
using the learning map.
"""

import sys

def display_greeting():
    """
    Formats and prints the program greeting.
    """
    # Init.
    title = " Skills progress "

    print("\n{:*^80s}\n".format(title.title()))
    print("\tThis program helps boot camp participants track their progress")
    print("\tusing the learning map.")
    print("\n{:*^80s}\n".format("*"))

def display_menu():
    print("\nMenu\n.")
    print("1. View all skills.")
    print("2. Mark items done.")
    print("3. View Progress.")
    print("4. View Incomplete skills.")

def get_the_input():
    """
    Get the input from the user.
    """
    while True:
        menu_num = input("\nEnter the menu number: ")
        if menu_num == "q":
            print("\nGoodbye")
            sys.exit()
        try:
            menu_num = int(menu_num)
        except ValueError:
            print("Invalid menu number")
            continue
        else:
            return menu_num

def view_skills(skills):
    """
    Formats and prints all the items in a dictionary.
    """
    num = 0
    for key, value in skills.items():
        print(str(key) + ". ", value)

def mark_items_done(skills, skills_done):
    """
    Accepts the skills, skills_not_done dictionaries and adds items in skills
    not done.
    """
    num_skill = input("Enter the number of skill done: ")
    for key, item in skills.items():
        if int(num_skill) == key:
            skills_done[key] = item
    return skills_done

def view_items_done(skills_done):
    """
    Accepts the value of skills)_done.
    """
    for key, value in skills_done.items():
        print(str(key) + ". ", value)

def view_incomplete_skills(skills, skills_done):
    skills_not_done = {}
    for key, value in skills_done.items():
        #for key_skill, value_skill in skills.items():
        if key, value not in skills_done.items():
            skills_not_done[key] = value
    
        
    for key, value in skills_not_done.items():
        print(str(key) + ". ", value)
    

def main():
    # Init.
    skills = {1: "Programming logic", 2: "Agile Methodology",
              3: "Test Driven Development", 4: "Git", 5: "OOP",
              6: "Programming logic"}
    skills_done = {}
    # Display the program greeting.
    display_greeting()

    # Display the program menu.
    display_menu()
    print()

    # Display all the skills.
    view_skills(skills)

    while True:
        # get the input from the user.
        menu_num = get_the_input()

        if menu_num == 1:
            view_skills(skills)
            print()
        elif menu_num == 2:
            mark_items_done(skills, skills_done)
            view_items_done(skills_done)
            print()
        elif menu_num == 3:
            view_items_done()
            print()
        elif menu_num == 4:
            view_incomplete_skills(skills, skills_done)
            print()
        else:
            print("\nNumber not in menu")
            display_menu()
            continue
        
        # Ask if the user wants to continue.
        while True:
            response = input("\nContinue? (y/n): ")
            if response in "yYnN":
                break
            print("Invalid response")
        if response.lower() == "n":
            print("\nGoodbye")
            break

if __name__ == "__main__":
    main()
