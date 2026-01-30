# Problem 56: Remove vowels from string
# Find and fix the error

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)

sentence = "Hello World"
print(f"Without vowels: {remove_vowels(sentence)}")

