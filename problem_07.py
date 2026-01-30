# Problem 7: Calculate factorial of a number
# Find and fix the error

def factorial(n):
    result = 1
    for i in range(1, n + 1):  # include n
        result *= i
    return result

print(f"Factorial of 5: {factorial(5)}")

