# Problem 48: Create a simple calculator
# Find and fix the error

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"

print(f"10 / 0 = {calculator(10, 0, 'divide')}")
