m, n = 19, 17

# 1. Все пути
dp_all = [[0]*(n+1) for _ in range(m+1)]
dp_all[0][0] = 1
for i in range(m+1):
    for j in range(n+1):
        if i > 0:
            dp_all[i][j] += dp_all[i-1][j]
        if j > 0:
            dp_all[i][j] += dp_all[i][j-1]

print("1. Всего кратчайших путей:", dp_all[m][n])

# 2. Без двух вверх подряд
dp0 = [[0]*(n+1) for _ in range(m+1)]
dp1 = [[0]*(n+1) for _ in range(m+1)]
dp0[0][0] = 1

for i in range(m+1):
    for j in range(n+1):
        if i > 0:
            dp0[i][j] += dp0[i-1][j] + dp1[i-1][j]
        if j > 0:
            dp1[i][j] += dp0[i][j-1]

result = dp0[m][n] + dp1[m][n]
print("2. Без двух команд вверх подряд:", result)