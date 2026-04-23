usernameAndPassword = {} 

def signup():
    username = input("Create a username: ")
    if username in usernameAndPassword:
        print("Username already exists.")
    else:
        password = input("Create a password: ")
        usernameAndPassword[username] = password
        print("Successful!")

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    # Check if username exists and password matches
    if username in usernameAndPassword and usernameAndPassword[username] == password:
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Invalid username or password.")

# Main program loop
while True:
    choice = input("\n1. Register\n2. Login\n3. Exit\nSelect option: ")
    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid selection.")
