class HashTableLinear:
    def __init__(self, size=200):
        self.size = size
        self.table = ['*'] * size

    def hash_function(self, key):
        return sum(ord(c) for c in str(key)) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        while self.table[index] != '*':
            index = (index + 1) % self.size
        self.table[index] = key

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for i, item in enumerate(self.table):
                f.write(f"{i}: {item}\n")


with open('input_hash.txt', 'r') as f:
    text = f.read()
words = text.split()

hash_lin = HashTableLinear()
for word in words:
    hash_lin.insert(word)

hash_lin.save_to_file('hash_linear.txt')