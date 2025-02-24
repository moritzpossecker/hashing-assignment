from hash_table import create_hash_table, add_to_hash_table, get_dominant_values, get_bucket_sizes
from hashing import hash_value
from text_processor import get_word_list
from matplotlib import pyplot as plt


def plot_table(table: list) -> None:
    dominant_words = get_dominant_values(table)
    bucket_sizes = get_bucket_sizes(table)

    plt.figure(figsize=(10, 5))
    bars = plt.bar(range(len(bucket_sizes)), bucket_sizes, color='blue', alpha=0.7)

    for i, bar in enumerate(bars):
        dominant_word_entry = dominant_words[i]
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 dominant_word_entry[0], ha='center', va='bottom', fontsize=8, rotation=45)

    plt.xlabel("Bucket Index")
    plt.ylabel("Number of Elements")
    plt.suptitle("Hash Table Distribution")
    plt.title(f"a: {a}, b: {b}, total words: {len(word_list)}")
    plt.show()



m_list = [30]
a = 10
b = 7

word_list = get_word_list('StringHashing_Schneewittchen.txt')

for m in m_list:
    hash_table = create_hash_table(m)

    for word in word_list:
        add_to_hash_table(hash_table, word, hash_value(word, a, b, m))

    plot_table(hash_table)
