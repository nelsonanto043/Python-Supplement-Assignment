# Problem 4: Find the largest number in a list
# Find and fix the error

numbers = [45, 12, 78, 34, 89, 23]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"Largest number is: {largest}")

