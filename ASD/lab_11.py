def quickSort(a, b, arr):
    if a >= b:
        return
    m = arr[(a + b) // 2]
    left = a - 1
    right = b + 1
    while True:
        left += 1
        right -= 1
        while arr[left] < m:
            left += 1
        while arr[right] > m:
            right -= 1
        if left >= right:
            break
        arr[left], arr[right] = arr[right], arr[left]
    left = right
    right += 1
    quickSort(a, left, arr)
    quickSort(right, b, arr)

mas = [int(i) for i in input('Введите последовательность: ').split()]
quickSort(0, len(mas) - 1, mas)
print(mas)