while True:
    # User Input
    full_name = input("Enter First & Last Name Separated by a SPACE: ")

    # Split the full name into parts
    split_names = full_name.split()
    
    # Check if exactly two parts are provided by user or not
    if len(split_names) != 2:
        print("Invalid Entry - You must enter both the First and Last name!") # Error Message
        continue   # Automatically repeat the program

    first_name, last_name = split_names # Assign the names correspondingly!

    # Check if both the names contain only alphabetic characters
    if not first_name.isalpha():
        print(f"Invalid Entry - First Name contains a numeric or non-alpha characters!") # Error Message
        continue  # Automatically repeat the program
    
    elif not last_name.isalpha():
        print(f"Invalid Entry - Last Name contains a numeric or non-alpha character!") # Error Message
        continue  # Automatically repeat the program
    
    # Check if both the names are different!
    if first_name.strip().lower() == last_name.strip().lower():
        print(f"Invalid Entry - First Name and Last Name are same, must be different!") # Error Message
        continue
    
    # Capitalize the first letter of each name
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()

    # Print the Checked names to STDIO/terminal.
    print(f"Name Entered: {first_name} {last_name}")
