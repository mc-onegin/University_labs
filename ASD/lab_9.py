def sift_down(s, start, end):
    max_index = start
    while True:
        left = 2*max_index + 1
        right = 2*max_index + 2
        maximum = max_index   
        if left < end and s[maximum] < s[left]:
            maximum = 2*max_index+1
        if right < end and s[maximum] < s[right]:
            maximum = right
        if maximum == max_index:
            break
        s[max_index], s[maximum] = s[maximum], s[max_index]
        max_index = maximum


s = [int(i) for i in input('Введите последовательность: ').split()]
for i in range(len(s)//2 - 1, -1, -1):
    sift_down(s, i, len(s))

for j in range(len(s) - 1, 0, -1):
    s[0], s[j] = s[j], s[0]
    sift_down(s, 0, j)
    
    
print(s)
    