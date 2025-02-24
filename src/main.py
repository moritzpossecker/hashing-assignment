from hash_table import create_hash_table, add_to_hash_table
from hashing import hash_value
from text_processor import get_word_list
from matplotlib import pyplot as plt

word_list = get_word_list('StringHashing_Schneewittchen.txt')

m = 30
a = 10
b = 1307

hash_table = create_hash_table(m)

for word in word_list:
    add_to_hash_table(hash_table, hash_value(word, a, b, m))

print(word_list)
print(len(word_list))

print(hash_table)

bucket_sizes = []
for bucket in hash_table:
    if bucket is None:
        bucket_sizes.append(0)
    else:
        bucket_sizes.append(len(bucket))

plt.figure(figsize=(10, 5))
plt.bar(range(len(bucket_sizes)), bucket_sizes, color='blue', alpha=0.7)
plt.xlabel("Bucket Index")
plt.ylabel("Number of Elements")
plt.suptitle("Hash Table Distribution")
plt.title("a: " + str(a) + ", b: " + str(b) + ", total words: " + str(len(word_list)))
plt.show()