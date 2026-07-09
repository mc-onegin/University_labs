from itertools import combinations

def divide(s, g):
    s = list(s)
    div_len = len(g)
    for i in range(len(s) - div_len + 1):
        if s[i] == '1':
            for j in range(div_len):
                s[i+j] = str((int(s[i+j]) + int(g[j])) % 2)
    return ''.join(s[-(div_len-1):]).zfill(div_len-1)

def encode(info):
    return info + divide(info + '0'*r, g)

def build_syndrome_table(g, n, t_max):

    table = {}
    total_vectors = 0
    
    for w in range(1, t_max + 1):
        count = 0
        for positions in combinations(range(n), w):
            E = ['0'] * n
            for pos in positions:
                E[pos] = '1'

            E_str = ''.join(E)
            S = divide(E_str, g)
            
            table[S] = E_str
            count += 1

            print(f"{S} --- {E_str}")
        
        print(f"  Вес {w}: {count} векторов")
        total_vectors += count
    
    print(f"Всего рассмотрено {total_vectors} векторов ошибок")
    print(f"Получено {len(table)} уникальных синдромов")
    return table

def find_collisions(err, g, n, max_e):
    target_S = divide(err, g)
    collisions = []
    
    for weight in range(1, max_e + 1):
        for positions in combinations(range(n), weight):
            E = ['0']*n
            for pos in positions:
                E[pos] = '1'
            E_str = ''.join(E)
            
            if divide(E_str, g) == target_S:
                collisions.append((E_str, positions))
    
    return collisions

def hamming_distance(a, b):
    return sum(1 for i in range(len(a)) if a[i] != b[i])


n, m = 15, 7
r = n - m
g = "111010001"

print("1. Порождающая матрица")
G = []
for i in range(m):
    vec = '0'*i + '1' + '0'*(m-i-1)
    row = encode(vec)
    G.append(row)
    print(' '.join(row))
print("\nКодовые слова:")
words = []
for i in range(1, 2**m):
    info = format(i, f'0{m}b')
    keyword = encode(info)
    words.append(keyword)


dists  = {}
min_d = 10000
for i in range(len(words)):
    for j in range(i+1, len(words)):
        dist = hamming_distance(words[i], words[j])
        key = f"{i}-{j}"
        dists[key] = dist
        min_d = min(min_d, dist)

for i, (pair, dist) in enumerate(list(dists.items())[:30]):
    print(f"{pair}: {dist}")


# m
# for i in range(len(words)):
#     for j in range(i+1, len(words)):
#         dist = 0
#         for k in range(len(words[i])):
#             if words[i][k] != words[j][k]:
#                 dist += 1
#         
#         dists[(i, j)] = dist
# print(dists)          

print("\n2. Минимальное расстояние:")
print(f"d_min = {min_d}")

print("\n3. Характеристики кода:")
print(f"Исправляет: {(min_d-1)//2}-кратные ошибки")
print(f"Обнаруживает: {min_d-1}-кратные ошибки")

max_e = (min_d-1)//2
max_i = min_d - 1
table = build_syndrome_table(g, n, max_e)
print('01101001' in table)
print(table['01101001'])
print('01010010' in table)

collision = find_collisions('010010011000000', g, n, max_i)
for i in range(len(collision)):
    print(collision[i])