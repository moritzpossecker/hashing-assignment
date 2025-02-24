def hash_value(value: str, a: int, b: int, m: int) -> int:
    return (a + b * to_integer(value)) % m


def to_integer(value: str) -> int:
    ord_sum = 0
    for c in value:
        ord_sum += ord(c)
    return ord_sum