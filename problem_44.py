# Problem 44: Print Fibonacci sequence
# Find and fix the error

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
