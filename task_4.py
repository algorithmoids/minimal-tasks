# Return `True` if the `array` is sorted. False otherwise.
#
# Constraints:
# 1 <= len(array) <= 1000
# 0 <= number <= 10000

from typing import List


def is_sorted(array: List[int]) -> bool:
    ...


if __name__ == "__main__":
    assert is_sorted([0, 1, 2, 3]) is True
    assert is_sorted([0, 1, 2, 3]) is True
    assert is_sorted([3, 2, 1, 0]) is False
    assert is_sorted([10, 55, 100, 17]) is False
    assert is_sorted([100, 33, 44, 55]) is False
    assert is_sorted([33, 44, 44, 55]) is True
    assert is_sorted([100, 200, 300, 400, 500, 600]) is True
    assert is_sorted([100]) is True
