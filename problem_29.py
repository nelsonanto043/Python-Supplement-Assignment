# Problem 29: Function with default argument
# Find and fix the error

def add_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_to_list(1))
print(add_to_list(2))
print(add_to_list(3))

