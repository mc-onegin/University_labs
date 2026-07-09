import math
import heapq
#0
with open('text_4_lab.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Длина исходного текста: {len(text)} символов")

letters_only = ''.join(ch for ch in text if ch.isalpha())

print(f"Длина текста (только буквы): {len(letters_only)} символов")
print(f"Уникальных букв: {len(set(letters_only))}")
#1
dict = {}

for ch in letters_only:
    dict[ch] = dict.get(ch, 0) + 1

for i in range(len(letters_only)-1):
    pair = letters_only[i:i+2]
    dict[pair] = dict.get(pair, 0) + 1

singles = [(k, v) for k, v in dict.items() if len(k) == 1]
singles.sort(key = lambda x: -x[1])

print("\n2. ЧАСТОТЫ ОДИНОЧНЫХ БУКВ:")
for ch, cnt in singles:
    prob = cnt / len(letters_only)
    print(f"'{ch}': {cnt:3} ({prob:.6f})")

pairs = [(k, v) for k, v in dict.items() if len(k) == 2]
pairs.sort(key=lambda x: -x[1])

print(f"\nЧАСТОТЫ ПАР БУКВ (всего {len(pairs)} пар):")
for pair, cnt in pairs:
    prob = cnt / (len(letters_only) - 1)
    print(f"'{pair}': {cnt:2} ({prob:.6f})")
#2
print("\n3. КОД ХАФФМАНА")

class Node:
    def __init__(self, ch = None, dict = 0):
        self.ch = ch
        self.dict = dict
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.dict < other.dict

nodes = [Node(ch, cnt) for ch, cnt in pairs]
heapq.heapify(nodes)

while len(nodes) > 1:
    a = heapq.heappop(nodes)
    b = heapq.heappop(nodes)
    merged = Node(dict = a.dict + b.dict)
    merged.left, merged.right = a, b
    heapq.heappush(nodes, merged)

def get_codes(node, code = "", codes = {}):
    if node.ch:
        codes[node.ch] = code
    else:
        get_codes(node.left, code + "0", codes)
        get_codes(node.right, code + "1", codes)
    return codes

codes = get_codes(nodes[0])
#print(codes)
#encoded = ''.join(codes[ch] for ch in letters_only)

def encode_text_by_pairs(text, codes):
    encoded = ""
    i = 0
    while i < len(text) - 1:
        pair = text[i:i+2]
        if pair in codes:
            encoded += codes[pair]
        else:
            encoded += codes.get(pair, '')
        i += 2
    return encoded

encoded = encode_text_by_pairs(letters_only, codes)
total_pairs_count = len(letters_only) - 1

print(f"Закодировано: {len(encoded)} бит")
print(f"Длина исходного текста: {len(letters_only)} букв")
print(f"Средняя длина кода: {len(encoded)/len(letters_only):.2f} бит/букву")
print(f"Пример кодов (первые 5): {list(codes.items())[:5]}")

# Шеннон
total = len(letters_only)
Sh = -sum((cnt/total) * math.log2(cnt/total) for _, cnt in singles if cnt > 0)
print(f"\nФормула Шеннона: {Sh:.3f} бит/букву")
print(f"Теоретический минимум: {Sh * total:.0f} бит")

unique_count = len(singles)
uniform_bits_per_char = 6
uniform_bits = uniform_bits_per_char * total

print(f"\nРавномерное кодирование:")
print(f"  Уникальных букв: {unique_count}")
print(f"  Битов на букву: {uniform_bits_per_char}")
print(f"  Всего бит: {uniform_bits}")

print(f"\nСравнение:")
print(f"  Равномерное: {uniform_bits} бит")
print(f"  Хаффман: {len(encoded)} бит")
print(f"  Выигрыш Хаффмана: {((uniform_bits - len(encoded)) / uniform_bits * 100):.1f}%")
print(f"  Эффективность Хаффмана: {(Sh * total / len(encoded) * 100):.1f}% от теоретического")
#3
print("\n4. LZW КОДИРОВАНИЕ")

def lzw_encode(data):
    unique_chars = sorted(set(data))
    dictionary = {ch: i for i, ch in enumerate(unique_chars)}
    next_code = len(dictionary)
    
    result = []
    w = ""
    
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c
    
    if w:
        result.append(dictionary[w])
    
    return result, dictionary

lzw_codes, lzw_dict = lzw_encode(letters_only)

max_code = max(lzw_codes)
bits_needed = math.ceil(math.log2(max(max_code + 1, 2)))
lzw_bits = len(lzw_codes) * bits_needed

print(f"Кодов: {len(lzw_codes)}")
print(f"Максимальный код: {max_code}")
print(f"Битов на код: {bits_needed}")
print(f"Всего бит LZW: {lzw_bits}")

print(f"\nИТОГОВОЕ СРАВНЕНИЕ:")
print(f"{'Метод':<15} {'Биты':<10} {'Бит/символ':<12}")
print("-" * 40)
print(f"{'Равномерный':<15} {uniform_bits:<10} {uniform_bits_per_char:<12.2f}")
print(f"{'Хаффман':<15} {len(encoded):<10} {len(encoded)/total:<12.2f}")
print(f"{'LZW':<15} {lzw_bits:<10} {lzw_bits/total:<12.2f}")
print(f"{'Минимум':<15} {Sh*total:<10.0f} {Sh:<12.2f}")
