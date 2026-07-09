s = [int(i) for i in input('Введите последовательность: ').split()]
gap = len(s)//2
while gap >= 1:
    for i in range(gap, len(s)):
        tmp = s[i]
        j = i
        while j >= gap and s[j - gap] > tmp:
            s[j] = s[j - gap]
            j -= gap 
        s[j] = tmp
    gap //= 2
print(s)