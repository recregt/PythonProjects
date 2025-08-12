import os
import string
import random
from pathlib import Path

APP_DIR = ".password-generator"
FILE_NAME = "passwords.txt"

home_dir = Path.home()
app_dir_path = home_dir / APP_DIR

if not app_dir_path.exists():
    app_dir_path.mkdir()

passwords_file_path = app_dir_path / FILE_NAME
file_name = passwords_file_path

passwords_list = []

def load_passwords():
    try:
        with open(file_name, 'r') as f:
            for line in f:
                passwords_list.append(line.strip())
    except FileNotFoundError:
        pass

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (5-128): "))
            if 5 <= length <= 128:
                return length
            else:
                print("Error: Password length must be between 5 and 128.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def get_character_sets():
    choices = {}
    prompts = {
        'lowercase': "Include lowercase letters? (y/n): ",
        'uppercase': "Include uppercase letters? (y/n): ",
        'numbers': "Include numbers? (y/n): ",
        'special': "Include special characters? (y/n): "
    }
    for key, prompt in prompts.items():
        while True:
            choice = input(prompt).lower()
            if choice in ('y', 'n'):
                choices[key] = choice
                break
            print("Error: Invalid input. Please enter 'y' or 'n'.")
    character_options = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'numbers': string.digits,
        'special': "!@#$%^&*()_+-=[]{}|;:,.<>?"
    }
    available_chars = ""
    for key, chars in character_options.items():
        if choices.get(key) == 'y':
            available_chars += chars
    if not available_chars:
        print("Error: You must select at least one character set.")
        return None
    return available_chars

def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    print(f"Your new password is: {password}")
    return password

def show_menu():
    print("""
--- Password Generator ---
1. Generate new password
2. View saved passwords
3. Exit
""")

def view_passwords():
    if not passwords_list:
        print("\nNo saved passwords found.")
        return
    print("\n--- Saved Passwords ---")
    for password in passwords_list:
        print(password)

def save_passwords():
    with open(file_name, 'w') as f:
        for password in passwords_list:
            f.write(password + '\n')
    print("Passwords saved successfully.")
    
def main():
    load_passwords()
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            length = get_password_length()
            if length is None:
                continue
            chars = get_character_sets()
            if chars is None:
                continue
            password = generate_password(length, chars)
            if password:
                passwords_list.append(password)
                if len(passwords_list) > 10:
                    del passwords_list[0]
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            save_passwords()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()