# import statements to encrypt and hide our strings: pw + un
import hashlib
import getpass

# empty dictionary. to store key values of pw + un
pw_mgr = {}

# create account function
def create_acct():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    pw_mgr[username] = hashed_password
    print("Account stored successfully!")

# login function
def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in pw_mgr.keys() and pw_mgr[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# menu to pick function 1 or 2
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_acct()
        elif choice == "2":
            login()
        elif choice == "0":
            break
    else:
        print("Invalid choice.")
    
# tells python which order to run its functions
if __name__ == "__main__":
    main()