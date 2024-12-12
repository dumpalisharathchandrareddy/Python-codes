userdata = {}

while True:
    first_name = input("Please Enter Your First Name: ")
    if not first_name:
        print("First Name cannot be empty, Please try again.")
        continue

    last_name = input("Please Enter Your Last Name: ")
    if not last_name:
        print("Last Name cannot be empty, Please try again.")
        continue

    username = input("Enter Username: ")
    if not username:
        print("Username cannot be empty. Please try again.")
        continue
    if username in userdata:
        print("Username already exists or in use, Please choose a different username.")
        continue

    password_1 = input("Enter Password: ")
    password_2= input("Re-enter Password: ")
    if not password_1 or not password_2:
        print("Password cannot be empty, Please try again.")
        continue
    if password_1 != password_2:
        print("Passwords do not match, Please try again.")
        continue
    
    print("User information collected:")
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Username:", username)
    print("Password:", password_1)

    
    add_or_reject= input("Do you want to add the info \n( Enter 'reject' for not to add to User data or any key to add! ): \n")
    if add_or_reject.lower() == 'reject':
        print("Not added to the User data! User information rejected, Please try again.")
        continue
    else:
        userdata[username] = [last_name, first_name, password_1]
        print("Added to dictionary!")
        print(userdata)
    

    quit_opt = input("Do you want to quit? Press 'q' or 'Q' to quit the application or any key to continue: ")
    if quit_opt.lower() == 'q':
        break
    
