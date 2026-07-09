def change_ways(coins, amount):
    dp = [1] + [0] * amount 
    for coin in coins:
        for i in range(coin, amount + 1): dp[i] += dp[i - coin]
    return dp[amount]
coins, amount = [1, 2, 5], 5
print(f"Способы разменять {amount}: {change_ways(coins, amount)}") # (1+1+1+1+1, 1+1+1+2, 1+2+2, 5)