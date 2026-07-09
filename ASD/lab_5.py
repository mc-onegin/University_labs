s = [int(i) for i in input('Введите последовательность: ').split()]
sorted_p = [s[0]]
for i in range(1, len(s)):
    left = 0
    for j in range(len(sorted_p), 0, -1):
        if s[i] < sorted_p[j-1]:
            left += 1
    sorted_p.insert(len(sorted_p)-left, s[i])
print(sorted_p)

