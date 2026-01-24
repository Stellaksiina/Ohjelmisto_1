tries = 0
while tries < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "python" and password == "rules":
        print("Welcome")
        break
    else:
        tries = tries + 1
        if tries < 5:
            print("Incorrect username or password. Please try again.")
        else:
            print("Access denied")


