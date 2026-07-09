def max_sum(arr):
    if not arr:
        return 0, -1, -1
    
    current_sum = arr[0]
    max_sum = arr[0]
    
    current_start = 0
    max_start = 0
    max_end = 0
    
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            current_start = i
        else:
            current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i
    
    return max_sum, max_start, max_end

arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum1, start1, end1 = max_sum(arr1)
print(f"Массив: {arr1}")
print(f"Максимальная сумма: {sum1}")
print(f"Подмассив: {arr1[start1:end1+1]}")
print(f"Индексы: [{start1}, {end1}]")
print()

arr2 = [-5, -2, -8, -1]
sum2, start2, end2 = max_sum(arr2)
print(f"Массив: {arr2}")
print(f"Максимальная сумма: {sum2}")
print(f"Подмассив: {arr2[start2:end2+1]}")
print(f"Индексы: [{start2}, {end2}]")
print()

arr3 = [1, 2, 3, 4]
sum3, start3, end3 = max_sum(arr3)
print(f"Массив: {arr3}")
print(f"Максимальная сумма: {sum3}")
print(f"Подмассив: {arr3[start3:end3+1]}")
print(f"Индексы: [{start3}, {end3}]")