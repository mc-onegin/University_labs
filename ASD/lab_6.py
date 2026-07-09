def index_minimal(s):
    mini = 2**20
    index = 0
    for i in range(len(s)):
        if s[i] < mini:
            mini = s[i]
            index = i
    return index

s = [int(i) for i in input('Введите последовательность: ').split()]
for i in range(len(s)-1):
    k = index_minimal(s[i::])
    s[i], s[k+i] = s[k+i], s[i]
print(s)