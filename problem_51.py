# Problem 51: Reverse words in a sentence
# Find and fix the error

def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

text = "Hello World"
print(f"Reversed words: {reverse_words(text)}")

