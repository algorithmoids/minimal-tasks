# Return `True` if the `number` is prime, otherwise `False`.
#
# Constraints:
# 1 <= number <= 10000


def is_prime(number: int) -> bool:
    ...


if __name__ == "__main__":
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(23) is True
    assert is_prime(1200) is False
    assert is_prime(1) is True
    assert is_prime(141) is False
    assert is_prime(2) is True
