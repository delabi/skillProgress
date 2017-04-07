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

def main():
    # Display the program greeting.
    display_greeting()

    while True:
        # Display the program menu.
        display_menu()
        
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
