# Skapa ett program som fungerar som en enkel telefonkatalog.
# Varje person i katalogen ska kunna ha flera telefonnummer, och varje nummer ska vara kopplat till en viss kategori (“mobil”, “hem”, “jobb”, etc). För att möjliggöra detta kan du använda nästlade dictionaries: ett dictionary som innehåller andra dictionaries.
# Data Structure: We will use nested dictionaries to store names and associated phone numbers with categories.
# Functions:
# Add, remove, and search for people.
# Add, remove, and update phone numbers for a person.
# User Interface: A menu-driven system for interaction.
# User experience: Sträva efter användarvänlighet och datasäkerhet: Fråga till exempel användaren om hen verkligen vill ta bort eller ersätta befintlig information.


# frivilliga utvidgningsmöjligheter, t.ex:
# - möjlighet att spara flera nummer under samma kategori
# - möjlighet att också spara adress och andra kontaktuppgifter
# - möjlighet att spara information permanent till fil, i JSON-format (se kapitel 12.3 i kursboken)

import json

# The main directory will store all people and their phone numbers
directory = {}


def print_menu():
    print("\nPhone Directory Menu:")
    print("1. Add a person")
    print("2. Remove a person")
    print("3. Show all people")
    print("4. Search for a person")
    print("5. Add a phone number")
    print("6. Remove a phone number")
    print("7. Update a phone number")
    print("8. Save directory to file")
    print("9. Load directory from file")
    print("10. List all phone numbers")  # New option
    print("0. Exit")


def add_person():
    name = input("Enter the person's name: ")
    if name in directory:
        print(f"{name} already exists in the directory.")
    else:
        directory[name] = {}
        print(f"{name} has been added to the directory.")


def remove_person():
    name = input("Enter the person's name to remove: ")
    if name in directory:
        confirm = input(f"Are you sure you want to remove {name}? (y/n): ")
        if confirm.lower() == 'y':
            del directory[name]
            print(f"{name} has been removed from the directory.")
        else:
            print("Removal cancelled.")
    else:
        print(f"{name} not found in the directory.")


def show_all_people():
    if directory:
        print("\nList of people in the directory:")
        for name in directory:
            print(name)
    else:
        print("The directory is empty.")


def search_person():
    name = input("Enter the person's name to search: ")
    if name in directory:
        print(f"\n{n} phone numbers:")
        for category, number in directory[name].items():
            print(f"{category.capitalize()}: {number}")
    else:
        print(f"{name} not found in the directory.")


def add_phone_number():
    name = input("Enter the person's name to add a phone number for: ")
    if name in directory:
        category = input("Enter the category (e.g., mobile, home, work): ").lower()
        number = input(f"Enter the phone number for {category}: ")

        # Check if the category already exists for the person
        if category in directory[name]:
            print(f"Warning: {category} number already exists for {name}.")
            confirm = input(f"Do you want to replace it? (y/n): ")
            if confirm.lower() == 'y':
                directory[name][category] = number
                print(f"The {category} number has been updated for {name}.")
            else:
                print("Phone number not updated.")
        else:
            directory[name][category] = number
            print(f"{category.capitalize()} number has been added for {name}.")
    else:
        print(f"{name} not found in the directory.")


def remove_phone_number():
    name = input("Enter the person's name to remove a phone number from: ")
    if name in directory:
        category = input("Enter the category of the phone number to remove: ").lower()
        if category in directory[name]:
            confirm = input(f"Are you sure you want to remove the {category} number for {name}? (y/n): ")
            if confirm.lower() == 'y':
                del directory[name][category]
                print(f"The {category} number has been removed for {name}.")
            else:
                print("Phone number removal cancelled.")
        else:
            print(f"{category} number not found for {name}.")
    else:
        print(f"{name} not found in the directory.")


def update_phone_number():
    name = input("Enter the person's name to update a phone number for: ")
    if name in directory:
        category = input("Enter the category of the phone number to update: ").lower()
        if category in directory[name]:
            new_number = input(f"Enter the new phone number for {category}: ")
            directory[name][category] = new_number
            print(f"The {category} number has been updated for {name}.")
        else:
            print(f"{category} number not found for {name}.")
    else:
        print(f"{name} not found in the directory.")


def save_to_file():
    with open("directory.json", "w") as file:
        json.dump(directory, file)
    print("Directory saved to file.")


def load_from_file():
    global directory
    try:
        with open("directory.json", "r") as file:
            directory = json.load(file)
        print("Directory loaded from file.")
    except FileNotFoundError:
        print("No saved directory found.")


def list_all_phone_numbers():
    all_numbers = []
    for name, categories in directory.items():
        for category, number in categories.items():
            all_numbers.append(f"{name} ({category}): {number}")

    if all_numbers:
        print("\nAll phone numbers in the directory:")
        for entry in all_numbers:
            print(entry)
    else:
        print("No phone numbers in the directory.")


def main():
    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
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
        elif choice == "10":
            list_all_phone_numbers()  # New option to list all phone numbers
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

