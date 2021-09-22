import sys
import math
from contextlib import redirect_stdout


def compute_closest_to_zero(ts):
    # Write your code here
    if ts == [] or len(ts) <= 0:
        return 0
    if min(ts) < 0 and max(ts) <0:
        return max(ts)
    if len(str(ts)) <= 1:
        return ts[0]
    value = min((abs(i), i) for i in ts)
    value = max(value)
    return value


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    n = int(input())
    ts = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        solution = compute_closest_to_zero(ts)
    print(solution)


if __name__ == "__main__":
    main()

