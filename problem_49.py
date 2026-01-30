# Problem 49: Find all divisors of a number
# Find and fix the error

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):   # include n
        if n % i == 0:
            divisors.append(i)
    return divisors

print(f"Divisors of 24: {find_divisors(24)}")

