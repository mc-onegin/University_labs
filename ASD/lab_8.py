def count_ofDigits(x):
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count

s = [int(i) for i in input('Введите последовательность: ').split()]
count = count_ofDigits(max(s))
for dig_pos in range(count):
    buckets = [[] for n in range(10)]
    for k in s:
        digit = (k // (10 ** dig_pos)) % 10
        buckets[digit].append(k)
    s = []
    for m in buckets:
        s.extend(m)
print(s)
    
