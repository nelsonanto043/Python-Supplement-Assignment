# Problem 55: Count frequency of each element
# Find and fix the error

def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq
