import sys
import math
from contextlib import redirect_stdout


def compute_multiples_sum(n):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    value = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
            value = value + i


    return value


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    n = int(input())
    with redirect_stdout(sys.stderr):
        res = compute_multiples_sum(n)
    print(res)


if __name__ == "__main__":
    main()
