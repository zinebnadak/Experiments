# Function normalize that takes a string and returns a version of the string where all characters that are not letters are removed, and all letters are converted to lowercase.
def normalize(text: str) -> str:
    return ''.join(char.lower() for char in text if char.isalpha() or char == " " )

#char.lower()               Convert each character to lowercase
#for char in text           Go through each character in the input string
#if char.isalpha() or char == " "  Keep only if it's an alphabetical letter and comprehension keeps spaces as actual characters
# "".join ()                   Joins all charachters into one single string



#Function takes a full name as input and returns the person's initials. Each initial is an uppercase letter followed by a period. Exceptions: "af", "av", "de", and "von" should be abbreviated with lowercase letters
exceptions = {"af", "av", "de", "von"}  #lowercase words that are treated as exceptions (not capitalized)

def extract_initials(name: str) -> str:
    parts = name.strip().split()    # Remove trailing spaces, then split the name into individual words
    initials = []       # This list will hold the initials

    for part in parts:
        if part.lower() in exceptions:  # Check if the lowercase version of the word is in the exceptions set
            initials.append(part.lower()[0] + ".") # Add the lowercase first letter followed by a dot
        else:
            initials.append(part.capitalize()[0] + ".") # Add the capitalized first letter followed by a dot

    return "".join(initials)  # Combine all initials into a single string and return it


# Function Checks if a password is sufficiently secure. The default parameter values mean that a password must be at least 8 characters long, contain both uppercase and lowercase letters (i.e., mixed case), and also include punctuation characters.
import string       #for string.punctuation
def check_password(password: str,
                   length: int = 8,     #Checks if the password has minimum lenght of 8
                   mixed_case: bool = True,     #Contains both uppercase and lowercase letters (if mixed_case is True)
                   punctuation: bool = True) -> bool:   #Contains punctuation (if punctuation is True)

    if len(password) < length:      # Check if the password is shorter than the required minimum length
        return False                # Too short, so it's invalid

    if mixed_case:          # If mixed_case is required, check for both upper and lower case letters
        has_upper = any(c.isupper() for c in password)       # Check if there is at least one uppercase letter
        has_lower = any(c.islower() for c in password)      # Check if there is at least one lowercase letter
        if not (has_upper and has_lower):                   # If either upper or lower case is missing, password is invalid
            return False

    if punctuation:         #check if the password contains at least one punctuation character
        if not any(c in string.punctuation for c in password):      # Check if any character in the password is in string.punctuation (eg. all weird charchters)
            return False

    return True      # If all checks pass, return True — the password is valid