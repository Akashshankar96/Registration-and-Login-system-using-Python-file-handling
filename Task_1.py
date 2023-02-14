import re
import getpass

def register():
    while True:
        username = input("Enter your email/username: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
            print("Invalid email/username. Please try again.")
            continue
        
        if username.count(".") == 1 and username.index(".") > username.index("@"):
            password = getpass.getpass("Enter a password (5-16 characters long, with at least one uppercase, one lowercase, one digit, and one special character): ")
            if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,16}$", password):
                print("Invalid password. Please try again.")
                continue
            
            with open("users.txt", "a") as file:
                file.write(f"{username},{password}\n")
            
            print("Registration successful!")
            break
        else:
            print("Invalid email/username. Please try again.")

def login():
    while True:
        username = input("Enter your email/username: ")
        password = getpass.getpass("Enter your password: ")
        
        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip().split(",")
                if line[0] == username and line[1] == password:
                    print("Login successful!")
                    return
            else:
                print("Invalid username or password.")
                choice = input("Enter 1 to register, 2 to try again, or q to quit: ")
                if choice == "1":
                    register()
                elif choice == "q":
                    break

while True:
    choice = input("Enter 1 to register, 2 to login, or q to quit: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "q":
        break
    else:
        print("Invalid choice.")
