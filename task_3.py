# Calculate sum of all the elements in the list that are bigger than `margin`.
# Without using `sum` functions.
#
# Constraints:
# 1 <= len(array) <= 1000
# 0 <= number <= 10000
# 0 <= margin <= 10000

from typing import List


def sum_high_numbers(array: List[int], margin) -> int:
    ...


if __name__ == "__main__":
    assert sum_high_numbers([5, 3, 8], 4) == 13
    assert sum_high_numbers([0, 1, 2, 3], 3) == 0
    assert sum_high_numbers([3, 2, 1, 0], 1) == 5
    assert sum_high_numbers([10, 55, 100, 17], 15) == 172
    assert sum_high_numbers([100, 33, 44, 55], 33) == 199
    assert sum_high_numbers([33, 44, 44, 55], 33) == 143
    assert sum_high_numbers([100, 200, 300, 400, 500, 600], 600) == 0
    assert sum_high_numbers([100, 200, 300, 400, 500, 600], 800) == 0
    assert sum_high_numbers([100, 200, 300, 400, 500, 600], 400) == 1100
