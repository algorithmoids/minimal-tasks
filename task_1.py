# Return max value from the array of numbers without using `max` function.
#
# Constraints:
# 1 <= len(numbers) <= 100
# 0 <= N <= 1000

from typing import List


def max_value(numbers: List[int]) -> int:
    ...


if __name__ == "__main__":
    assert max_value([1, 3, 6, 8]) == 8
    assert max_value([10, 2, 13, 4]) == 13
    assert max_value([100, 17, 35, 4]) == 100
    assert max_value([3, 50]) == 50
    assert max_value([42]) == 42
