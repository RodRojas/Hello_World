##Write a password generator in Python. Be creative
##with how you generate passwords - strong passwords
##have a mix of lowercase letters, uppercase letters,
##numbers, and symbols. The passwords should be random,
##generating a new password every time the user asks for
##a new password. Include your run-time code in a main method.

import random
import string

def get_password_length():
    password_length = input("how long should your password be? ")
    password_length = int(password_length)
    return password_length

def password():
    password_length = get_password_length()
    a = string.ascii_lowercase
    b = string.ascii_uppercase
    c = string.punctuation
    d = string.digits
    characters = (a+b+c+d)*1000
    characters = list(characters)
    random.shuffle(characters)
    password = random.sample(characters, password_length)
    password = ''.join(password)
    print(password)

password()
   
    
