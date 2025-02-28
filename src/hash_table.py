def create_hash_table(l: int) -> list:
    return list(None for _ in range(l))


def add_to_hash_table(hash_table: list, value: str, key: int) -> None:
    if hash_table[key] is None:
        hash_table[key] = []

    hash_table[key].append(value)


def get_bucket_sizes(hash_table: list) -> list:
    bucket_sizes = []
    for bucket in hash_table:
        if bucket is None:
            bucket_sizes.append(0)
        else:
            bucket_sizes.append(len(bucket))
    return bucket_sizes


def get_dominant_values(hash_table: list) -> list:
    dominant_values = []
    for bucket in hash_table:
        if bucket is None:
            dominant_values.append(['', 0, 0])
            continue

        most_common_word = max(set(bucket), key=bucket.count)
        count = bucket.count(most_common_word)
        dominant_values.append([most_common_word, count, int((count / len(bucket)) * 100)])

    return dominant_values
