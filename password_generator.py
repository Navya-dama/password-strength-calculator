import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[A-Z]", password):
        return "Weak: Add uppercase letters"
    if not re.search("[a-z]", password):
        return "Weak: Add lowercase letters"
    if not re.search("[0-9]", password):
        return "Weak: Add digits"x
    if not re.search("[@#$%^&*!]", password):
        return "Weak: Add special characters"
    return "Strong Password "

password = input("Enter your password: ")
print(check_password_strength(password))
