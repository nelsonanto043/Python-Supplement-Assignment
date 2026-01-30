# Problem 40: Count consonants in a string
# Find and fix the error

def count_consonants(text):
    vowels = set("aeiouAEIOU")
    return sum(1 for c in text if c.isalpha() and c not in vowels)

