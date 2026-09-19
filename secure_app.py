# Secure Login Example

import hashlib
import getpass

stored_password = hashlib.sha256("12345".encode()).hexdigest()

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

password_hash = hashlib.sha256(password.encode()).hexdigest()

if username == "admin" and password_hash == stored_password:
    print("Login successful!")
else:
    print("Invalid username or password.")