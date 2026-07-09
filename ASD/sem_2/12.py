def backpack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        w_i = weights[i - 1]
        v_i = values[i - 1]
        for w in range(capacity + 1):
            if w_i <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - w_i] + v_i)
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], selected


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, items = backpack(weights, values, capacity)
print(f"Максимальная стоимость: {max_value}")
print(f"Выбранные предметы (индексы): {items}")
print(f"Их веса: {[weights[i] for i in items]}")
print(f"Их стоимости: {[values[i] for i in items]}")