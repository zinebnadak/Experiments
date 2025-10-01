def print_menu():
    # Prints the program menu.
    print("\nWelcome to the String Lab!")
    print("1. Check palindrome")
    print("2. Extract initials")
    print("3. Check password")
    print("4. Normalize text")
    print("5. Exit")

def get_menu_choice(no_of_choices: int) -> int:
    # Gets the user's menu choice and validates it.
    while True:# Loop until valid input is received
        try:
            choice = int(input(f"Choose an option (1-{no_of_choices}): "))# Ask user to enter a number between 1 and no_of_choices
            if 1 <= choice <= no_of_choices:# Check if the number is within the valid range
                return choice# Valid input, return the choice
            else:
                print(f"Invalid choice! Please enter a number between 1 and {no_of_choices}.")# If number is outside valid range, show error and loop again
        except ValueError:# If input was not a number (e.g., user typed "hello"), catch the error
            print("Invalid input! Please enter a number.")
print()
