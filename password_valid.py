print("Welcome to Lefa Jele-Masemola's Password Validator >>>")


# Initialize criteria for password 
min_length = 6
max_length = 10
special_characters = "$#@"

# Initializing  flags
has_lower = False
has_upper = False
has_digit = False
has_special = False

# Prompt for user's name and surname
name = input("Enter your name: ")
surname = input("Enter your surname: ")

while True:
    #Prompt user to insert a password
    password = input("Please enter a new password: ")
    
    # Reset flags for each new password attempt, user can have as many attempts until it mets requirements
    lower_case = False
    upper_case = False
    num = False
    special_char = False
    
    # Check length criteria
    length = 0
    for char in password:
        length += 1
    if length < min_length:
        print("Password must be at least 6 characters long.")
        continue
    if length > max_length:
        print("Password must be no more than 10 characters long.")
        continue

    # Iterate over each character in the password
    py = 0 #lol it't not law to use i
    while py < length:
        char = password[py]
        if 'a' <= char <= 'z':
            lower_case = True
        if 'A' <= char <= 'Z':
            upper_case = True
        if '0' <= char <= '9':
            num = True
        if char == '$' or char == '#' or char == '@':
            special_char = True
        py += 1

    # Check if all criteria are met
    if lower_case == False:
        print("Password must include at least one lowercase letter (a-z).")
        continue
    if upper_case == False:
        print("Password must include at least one uppercase letter (A-Z).")
        continue
    if num == False:
        print("Password must include at least one digit (0-9).")
        continue
    if special_char == False:
        print("Password must include at least one special character from $#@.")
        continue

    print(f"Password is valid. Welcome, {name} {surname}!")
    break

input("Please press Enter to Exit...")