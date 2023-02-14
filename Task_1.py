# Register

def register():
    # Get email/username
    email = input("Enter your email/username: ")

    # Validate email/username
    if "@" in email or "." in email:
        print("Invalid email/username. Please try again.")
        return register()

    # Get password
    password = input("Enter your password: ")

    # Validate password
    if len(password) < 5 or len(password) > 16:
        print("Invalid password. Please try again.")
        return register()
    if not any(char.isdigit() for char in password):
        print("Invalid password. Please include at least one digit.")
        return register()
    if not any(char.isupper() for char in password):
        print("Invalid password. Please include at least one uppercase character.")
        return register()
    if not any(char.islower() for char in password):
        print("Invalid password. Please include at least one lowercase character.")
        return register()
    if not any(not char.isalnum() for char in password):
        print("Invalid password. Please include at least one special character.")
        return register()

    # Save email/username and password to file
    with open("user_data.txt", "w") as file:
        file.write(email + "," + password)
    print("Registration successful!")


# Login
def login():
    # Get email/username
    email = input("Enter your email/username: ")

    # Check if email/username exists in file
    with open("user_data.txt", "r") as file:
        data = file.read()
        if email not in data:
            print("Email/username not found. Please try again or register.")
            return

    # Get password
    password = input("Enter your password: ")

    # Check if password is correct
    with open("user_data.txt", "r") as file:
        data = file.read().split(",")
        if data[1] != password:
            print("Incorrect password. Please try again or use the 'forgot password' feature.")
            return

    # Login successful
    print("Login successful!")
