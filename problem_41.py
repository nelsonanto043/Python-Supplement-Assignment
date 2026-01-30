# Problem 41: Find index of element in list
# Find and fix the error

numbers = [10, 20, 30, 40, 50]
search = 30

if search in numbers:
    print(f"Index of {search}: {numbers.index(search)}")
else:
    print("Element not found")

