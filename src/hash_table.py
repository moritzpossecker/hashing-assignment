def create_hash_table(l: int) -> list:
    return list(None for _ in range(l))

def add_to_hash_table(hash_table: list, key: int) -> None:
    if hash_table[key] is None:
        hash_table[key] = []

    hash_table[key].append(key)