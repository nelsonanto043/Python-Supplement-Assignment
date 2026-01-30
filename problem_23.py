# Problem 23: Count positive and negative numbers
# Find and fix the error

numbers = [12, -5, 8, -3, 15, -9, 0]
positive = 0
negative = 0
for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
print(f"Positive: {positive}")
print(f"Negative: {negative}")
