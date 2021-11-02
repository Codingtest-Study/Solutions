# 합분해 점화식 유도
# DP[i][j] = DP[i][j-1] + (DP[i-1][j-1] + DP[i-2][j-1] + .... + DP[0][j-1])
# DP[i-1][j-1] + DP[i-2][j-1] + .... + DP[0][j-1] = DP[i-1][j] 
# DP[i][j] = DP[i][j-1] + DP[i-1][j]

import sys
input = sys.stdin.readline
n, k = map(int, input().split())

DP = [[0]*(k+1) for _ in range(n+1)]    
for i in range(k+1):
    DP[0][i] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        DP[i][j] = (DP[i][j-1] + DP[i-1][j])%1000000000

print(DP[n][k])