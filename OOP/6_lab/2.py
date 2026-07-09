n = int(input())
a = list(map(int, input().split()))
ops = list(map(int, input().split()))

pref_min = [0] * n
pref_min[0] = a[0]
for i in range(1, n):
    pref_min[i] = min(pref_min[i-1], a[i])

suf_min = [0] * n
suf_min[n-1] = a[n-1]
for i in range(n-2, -1, -1):
    suf_min[i] = min(suf_min[i+1], a[i])

l = 0
r = n - 1
result = []

for op in ops:
    cur_min = min(pref_min[r], suf_min[l])
    result.append(cur_min)
    
    if op == 0:
        l += 1
    else:
        r -= 1

print(*result)