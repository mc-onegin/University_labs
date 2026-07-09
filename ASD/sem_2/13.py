def first_fit(items, bin_capacity):
    bins = []
    
    for item in items:
        placed = False
        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                placed = True
                break

        if not placed:
            bins.append(item)
    
    return bins


items = [2, 5, 4, 7, 1, 3, 8] # в идеале [2, 8], [5, 4, 1], [7, 3]
capacity = 10

bins = first_fit(items, capacity)
print(f"Количество ящиков: {len(bins)}")
print(f"Заполнение ящиков: {bins}")
print(f"Сумма проверка: {sum(bins) == sum(items)}")

