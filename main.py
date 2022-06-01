#!/usr/bin/env python3

"""
~
Author @Codex-ops
~
"""

# Modules
import os
import string 
import random 
import hashlib
import pyfiglet

banner = pyfiglet.figlet_format("HasherPY")
print(banner)

password_length = int(input("enter password length: ")) # Takes user input amount

# Generate a randomly encrypted password
chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for index in range(password_length):
    password = password + random.choice(chars)

# Hashes Password above ^ 
a_string = password

hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()

# Outputs hashed & normal password in files 
def file():
    os.mkdir("passwords")
    os.chdir("passwords")
    a = open("hashes.txt", "a")
    a.write(hashed_string + "\n")
    a.close()

    b = open("password.txt", "a")
    b.write(password + "\n")
    b.close()
file()
