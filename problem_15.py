# Problem 15: Convert temperature from Celsius to Fahrenheit
# Find and fix the error

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    
    return fahrenheit

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")
