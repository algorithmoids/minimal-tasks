# Return `True` if the `number` is even, otherwise `False`.
#
# Constraints:
# 0 <= number <= 10000


def is_even(number: int) -> bool:
    ...


if __name__ == "__main__":
    assert is_even(0) is True
    assert is_even(1200) is True
    assert is_even(1) is False
    assert is_even(141) is False
    assert is_even(2) is True
