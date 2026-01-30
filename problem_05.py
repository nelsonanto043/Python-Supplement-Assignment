text = "Hello World"
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
