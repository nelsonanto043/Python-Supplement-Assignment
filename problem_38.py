# Problem 38: Find sum of digits
# Find and fix the error

def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10   
    return total

print(f"Sum of digits of 12345: {sum_of_digits(12345)}")

