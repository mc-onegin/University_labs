def cnt(e = 2, n = 100):
    dp = [[0]*(n+1) for _ in range(e+1)]
    for i in range(1, e+1):
        dp[i][1] = 1
        for f in range(1, n+1):
            if i == 1:
                dp[i][f] = f
            elif f > 1:
                dp[i][f] = min(1 + max(dp[i-1][k-1], dp[i][f-k]) for k in range(1, f+1))
    return dp[e][n]
    
print(cnt())