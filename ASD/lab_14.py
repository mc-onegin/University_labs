class HashTableChaining:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(c) for c in str(key)) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for i, bucket in enumerate(self.table):
                f.write(f"{i}: {bucket}\n")
                

with open('input_hash.txt', 'r') as f:
    text = f.read()
words = text.split()

hash_chain = HashTableChaining()
for word in words:
    hash_chain.insert(word)

hash_chain.save_to_file('hash_chaining.txt')