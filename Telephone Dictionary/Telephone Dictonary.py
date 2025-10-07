#TELEPHONE DICTIONARY
#Create a program that functions as a basic phonebook. Each person in the phonebook can have multiple phone numbers, and each number is associated with a specific category (e.g., "mobile," "home," "work," etc.). To represent this, nested dictionaries will be used to store the data.
#Core Functions:
# Add Person
# Remove Person
# show all *people
# Search for Person
# Add Phone Number
# Remove Phone Number
# Update Phone Number

# and for JSON:
# Save data
# Load data

# User Interface: menu-driven, allowing the user to choose from the available functions.
# User Experience and data security :Ask for confirmation before any data deletion or replacement.

# + be able to save Multiple phone numbers in the same category

import json

# The main directory will store all people and their phone numbers
directory = {}


def print_menu():               #UI= User Interface
    print("\nPhone Directory Menu:")
    print("1. Add a person")
    print("2. Remove a person")
    print("3. Show all people")
    print("4. Search for a person")
    print("5. Add a phone number")
    print("6. Remove a phone number")
    print("7. Update a phone number")
    print("8.  Save data")
    print("9. Load data")
    print("0. Exit")


def add_person():
    name = input("Enter the person's name: ")
    if name in directory:
        print(f"{name} already exists in the directory.")
    else:
        directory[name] = {}        #If the if condition is False, directory[name] = {} creates a new entry in the directory dictionary for that name (using name as the key) and assigns an empty dictionary {} as the value. This empty dictionary will later store the person's phone numbers.
        print(f"{name} has been added to the directory.")


def remove_person():
    name = input("Enter the person's name to remove: ")
    if name in directory:
        confirm = input(f"Are you sure you want to remove {name}? (y/n): ")
        if confirm.lower() == 'y':      #not case sensitive , acceps y and Y
            del directory[name]     #deletes the entry for the specified name from the directory dictionary. After deleting the entry, a message is printed to let the user know
            print(f"{name} has been removed from the directory.")
        else:
            print("Removal cancelled.")
    else:
        print(f"{name} not found in the directory.")        #if the user entered non existing person get this


def show_all_people():
    if directory:       #This line checks if the directory is not empty, eg. True - it will execute code below
        print("\nList of people in the directory:")
        for name in directory:      #loop trough the directory and print all the KEYS (eg. names)
            print(name)
    else:
        print("The directory is empty.")    #if directory if False

def search_person():
    name = input("Enter the person's name to search: ")
    if name in directory:       #This checks if the entered name exists as a key in the directory dictionary.
        print(f"\n{name} phone numbers:")       #print a message stating that it's displaying the phone numbers for that person.
        for category, numbers in directory[name].items():       #begins a loop that iterates over the phone numbers associated with the person. returns the dictionary of phone numbers (which is a dictionary with categories as keys and lists of phone numbers as values). .items() is used to iterate through each category ( "mobile", "home", "work")
            for number in numbers:      #For each category, the code iterates through all the phone numbers in the list numbers.
                print(f"{category.capitalize()}: {number}")     #category.capitalize() capitalizes the first letter of the category (e.g., "mobile" becomes "Mobile"), kunde skippas men valde göra såhär
    else:
        print(f"{name} not found in the directory.")


def add_phone_number():
    name = input("Enter the person's name to add a phone number for: ")
    if name in directory:
        category = input("Enter the category (e.g., mobile, home, work): ").lower()
        number = input(f"Enter the phone number for {category}: ")

        # Check if the category already exists for the person
        if category in directory[name]:
            if number not in directory[name][category]:     #if the category exists and the phone number is not already in the list for that category, the phone number is appended to the list of phone numbers for that category using append()
                directory[name][category].append(number)
                print(f"The {category} number has been added for {name}.")      #confirmation message is printed
            else:
                print(f"The {category} number already exists for {name}.")
        else:
            directory[name][category] = [number]
            print(f"The {category} number has been added for {name}.")      #confirmation message is printed
    else:
        print(f"{name} not found in the directory.")


def remove_phone_number():
    name = input("Enter the person's name to remove a phone number from: ")
    if name in directory:           #This checks whether the entered name (name) exists in the directory dictionary.
        category = input("Enter the category of the phone number to remove: ").lower()
        if category in directory[name]:     #This checks if the category (e.g., "mobile", "home", etc.) exists in the directory for that specific person (directory[name]).
            print(f"Current {category} numbers: {directory[name][category]}")       #If the category exists for the person, this line prints the current list of phone numbers under that category.
            number = input(f"Enter the phone number to remove from {category}: ")
            if number in directory[name][category]:     #This checks if the entered number exists in the list of phone numbers under the specified category (directory[name][category])
                directory[name][category].remove(number)
                print(f"The {category} number has been removed for {name}.")
            else:
                print(f"The number {number} is not found in the {category} category.")
        else:
            print(f"No {category} number found for {name}.")
    else:
        print(f"{name} not found in the directory.")


def update_phone_number():
    name = input("Enter the person's name to update a phone number for: ")
    if name in directory:
        category = input("Enter the category of the phone number to update: ").lower()
        if category in directory[name]:
            print(f"Current {category} numbers: {directory[name][category]}")       #If the category exists for that person, print the current list of phone numbers associated with that category for the person.
            old_number = input(f"Enter the old phone number to replace in {category}: ")        #The user is prompted to enter the old phone number they wish to replace in the specified category
            if old_number in directory[name][category]:             #checks if the entered old phone number exists in the list of phone numbers for that category under the specified person's name (directory[name][category])
                new_number = input(f"Enter the new phone number for {category}: ")
                index = directory[name][category].index(old_number)     #The index of the old number is found using the .index() method
                directory[name][category][index] = new_number           #The old number is replaced with the new number at the same index in the list of phone numbers for the specified category.
                print(f"The {category} number has been updated for {name}.")
            else:
                print(f"The number {old_number} is not found in the {category} category.")
        else:
            print(f"{category} number not found for {name}.")
    else:
        print(f"{name} not found in the directory.")



def save_to_file():
    with open("phonebook.json", "w") as file:       #to open a file named phonebook.json in write mode. in JSON If the file already exists, it will be overwritten; if the file does not exist, a new file will be created.
        json.dump(directory, file)                  #used to serialize/convert the directory dictionary into JSON format and write it to the file.
    print("Data saved to phonebook.json")


def load_from_file():
    global directory            #global is used to indicate that we are referring to the directory variable that is defined outside the function
    try:
        with open("phonebook.json", "r") as file:       #to open the phonebook.json file in read mode
            directory = json.load(file)                 #eads the JSON data from the file and deserializes it into a Python object (in this case, a dictionary)
        print("Data loaded from phonebook.json")
    except FileNotFoundError:
        print("No saved data found.")                   #If the phonebook.json file does not exist ( because the program has never saved data before), a Error is raised.


def main():
    while True:         #loop keeps the program running continuously until the user chooses to exit.
        print_menu()    #prints the menu of available options
        choice = input("Choose an option: ")        #takes the user's input and assigns it to the variable choice

        if choice == "1":           #the user can only pick one option at a time, and once one option is selected, the rest don’t need to be evaluated.
            add_person()
        elif choice == "2":
            remove_person()
        elif choice == "3":
            show_all_people()
        elif choice == "4":
            search_person()
        elif choice == "5":
            add_phone_number()
        elif choice == "6":
            remove_phone_number()
        elif choice == "7":
            update_phone_number()
        elif choice == "8":
            save_to_file()
        elif choice == "9":
            load_from_file()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":      #__name__ is a special variable that determines if the script is run directly or imported. ensures that the code inside it only runs when the script is executed directly (not when imported).
    main()
