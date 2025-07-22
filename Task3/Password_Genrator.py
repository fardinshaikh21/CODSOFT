import random

def generate_password(length):
    
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    all_characters = uppercase_letters + lowercase_letters + digits + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

try:
    password_length = int(input("Enter the desired password length: "))
    
    if password_length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(password_length)
        print("Generated Password : ", password)

except ValueError:
    print("Please enter a valid number.")
