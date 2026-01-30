# Problem 17: Capitalize first letter of each word
# Find and fix the error

def capitalize_words(text):
    
    words = text.split()
    capitalized = []
    for word in words:
        capitalized.append(word.capitalize())
    return " ".join(capitalized)

sentence = "hello world from python"
print(capitalize_words(sentence))
