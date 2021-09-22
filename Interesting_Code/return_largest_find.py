# Python code below
# Use print("messages...") to debug your solution.

def find_largest(numbers):
    if len(str(numbers)) <= 1:
        return numbers[0]
    value = 0
    for i in numbers:
        if abs(i) > abs(value):
            value = i

    # Your code goes here
    return value
