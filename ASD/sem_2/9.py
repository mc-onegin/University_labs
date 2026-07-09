def tsp(dist, cities_set):
    cities = list(cities_set)
    n = len(cities)
    
    if n <= 1:
        return 0
    
    INF = 10**9
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    
    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] < INF:
                for j in range(n):
                    if not (mask & (1 << j)):
                        cost = dist[cities[i]][cities[j]]
                        dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + cost)
    
    result = INF
    full_mask = (1 << n) - 1
    for i in range(n):
        result = min(result, dp[full_mask][i] + dist[cities[i]][cities[0]])
    
    return result if result < INF else -1

dist = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 40],
    [20, 25, 30, 0, 35],
    [25, 30, 40, 35, 0]
]

cities_to_visit = {0, 4, 2}
result = tsp(dist, cities_to_visit)
print(f"Минимальный путь для городов {cities_to_visit}: {result}")