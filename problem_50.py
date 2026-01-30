# Problem 50: Convert string to uppercase
# Find and fix the error

from email.mime import text


text = "python programming"
uppercase = ""

for char in text:
    # If char is a lowercase letter
    if 'a' <= char <= 'z':
        uppercase += chr(ord(char) - 32)  # Convert to uppercase
    else:
        uppercase += char  # Keep other characters as-is

print(f"Uppercase: {uppercase}")

