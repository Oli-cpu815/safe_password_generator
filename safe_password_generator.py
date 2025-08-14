#!/usr/bin/env python3

import random
import string

def get_user_input(prompt, default="y"):
    response = input(f"{prompt} (Y/n): ").strip().lower()
    if response == "":
        return default.lower() == "y"
    return response == "y"

def get_password_length():
    while True:
        try:
            length = int(input("Enter Password Length You Want (e.g.4,6,8): "))
            if length <= 0:
                print("❌ Password length must be greater than 0.")
            else:
                return length
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected!")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("🔐 Safe Password Generator 🔐\n")

    length = get_password_length()
    use_upper = get_user_input("Include uppercase letters?")
    use_lower = get_user_input("Include lowercase letters?")
    use_digits = get_user_input("Include digits?")
    use_symbols = get_user_input("Include special characters?")

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print("\n✅ Your Generated Password:\n" + password)
    except ValueError as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()



