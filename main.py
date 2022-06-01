#!/usr/bin/env python3

"""
~
Author @Codex-ops
~
"""
# Modules
import string 
import random 
import hashlib

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
    a = open("hashes.txt", "a")
    a.write("" + hashed_string)
    a.close()

    b = open("password.txt", "a")
    b.write("" + password)
    b.close()
file()
