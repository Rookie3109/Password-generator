# Write a program to generate a random password with 2 uppercase letters, 2 lowercase letters, 2 symbols, 2 numbers. Extend it to creating a password with first character as uppercase


import random

lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@_$%^&"


def generate_password():
    lower = random.sample(lower_letters, 2)
    upper = random.sample(upper_letters, 2)
    num = random.sample(range(0, 9), 2)
    sym = random.sample(symbols, 2)
    _password = upper + lower + num + sym
    random.shuffle(_password)
    password = "".join(map(str, _password))
    return password
