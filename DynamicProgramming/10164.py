# 격자상의 경로
# https://www.acmicpc.net/problem/10164

n, m, k = map(int, input().split())
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

if k > 0:
    x, y = (k - 1) // m, (k - 1) % m
else:
    x, y = n - 1, m - 1

for i in range(x + 1):
    for j in range(y + 1):
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
for i in range(x, n):
    for j in range(y, m):
        if i == x and j == y: continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]

print(dp[n - 1][m - 1])