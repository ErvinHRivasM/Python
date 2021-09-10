# Python code below
# Use print("messages...") to debug your solution.
# Test Code // print(Answer.find_largest([1,789]))  # 200

def find_largest(numbers):
    # Your code goes here
    tmp = 0
    if len(numbers) == 1:
        return numbers[0]
    else:
        for n in numbers:
            if(n > tmp):
                tmp = n
    return tmp


#---------------------------------------------#
#---------------------------------------------#
#---------------------------------------------#


import sys
import math
from contextlib import redirect_stdout


def compute_closest_to_zero(numbers):
    # Write your code here
    if numbers == []:
        return 0
    tmp = max(numbers)
    if len(numbers) == 1:
        return abs(numbers[0])
    else:
        for n in numbers:
            print(n)
            n = abs(n)
            if(n < tmp):
                tmp = n
    return tmp



# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    solution = 0
    n = int(input())
    ts = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        solution = compute_closest_to_zero(ts)
    print(solution)


if __name__ == "__main__":
    main()
