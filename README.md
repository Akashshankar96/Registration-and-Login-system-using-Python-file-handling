
# Registration and Login system using Python, file handling
This program implements a Registration and Login system using Python and file handling. Users can register with a valid email/username and password, and their information will be stored in a text file called users.txt. Users can also login with their email/username and password, and the program will check whether their credentials exist in the file or not.


## Requirements
This program requires Python 3.6 or later to run.

## Usage




TO run the program, open a command prompt or terminal window and navigate to the directory where the code is saved. Then, enter the following command:
```bash
  python registration_and_login.py
```


This will start the program and display a menu with three options: register, login, or quit. To choose an option, enter the corresponding number (1 for register, 2 for login, or q for quit) and press Enter.

If you choose to register, you will be prompted to enter your email/username and password. The program will check whether they meet the specified requirements and write your information to the users.txt file if they are valid.

If you choose to login, you will be prompted to enter your email/username and password. The program will check whether they match any in the users.txt file. If your input is invalid, you will be given the option to register, try again, or quit.


## Example

Here is an example of how to use the program:

```bash
  $ python registration_and_login.py
1. Register
2. Login
q. Quit
Enter your choice: 1
Enter your email/username: john@gmail.com
Enter a password (5-16 characters long, with at least one uppercase, one lowercase, one digit, and one special character):
Registration successful!

1. Register
2. Login
q. Quit
Enter your choice: 2
Enter your email/username: john@gmail.com
Enter your password:
Login successful!

1. Register
2. Login
q. Quit
Enter your choice: q

```
