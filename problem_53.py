# Problem 53: Check if two strings are anagrams
# Find and fix the error

def are_anagrams(str1, str2):
    # Convert both strings to lowercase before sorting
    return sorted(str1.lower()) == sorted(str2.lower())

word1 = "Listen"
word2 = "Silent"
print(f"Are anagrams: {are_anagrams(word1, word2)}")  # True

