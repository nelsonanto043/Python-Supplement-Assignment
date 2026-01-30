# Problem 20: Find common elements in two lists
# Find and fix the error

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for item in list1:
    if item in list2:

        common.append(item)
print(f"Common elements: {common}")
