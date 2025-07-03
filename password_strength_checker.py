# password_strength_checker.py

import re

def check_password_strength(password):
    """
    Checks the strength of a given password based on:
    - Minimum 8 characters
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one special character
    """
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."
    
    return "Strong: Your password is secure!"

def password_checker():
    
    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")
        
        if password.lower() == "exit":
            print("Thank you for using the Password Strength Checker!")
            break
        
        result = check_password_strength(password)
        print(result)

if __name__ == "__main__":
    password_checker()
