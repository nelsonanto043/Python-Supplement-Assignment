# Problem 37: Check if year is leap year
# Find and fix the error

def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

print(f"Is 2014 a leap year? {is_leap_year(2014)}")
