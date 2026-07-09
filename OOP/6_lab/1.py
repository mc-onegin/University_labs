import heapq

n = int(input())
a = list(map(int, input().split()))
ops = list(map(int, input().split()))

heap = a[:]
heapq.heapify(heap)

deleted = {}
left = 0
right = n - 1
res = []

for op in ops:
    while heap and deleted.get(heap[0], 0):
        x = heapq.heappop(heap)
        deleted[x] -= 1
        if deleted[x] == 0:
            del deleted[x]
    
    res.append(heap[0])
    
    if op == 0:
        x = a[left]
        deleted[x] = deleted.get(x, 0) + 1
        left += 1
    else:
        x = a[right]
        deleted[x] = deleted.get(x, 0) + 1
        right -= 1

print(' '.join(map(str, res)))
