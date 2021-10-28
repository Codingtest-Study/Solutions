# 1. 퇴사 14501 - 실버 3
import sys
input = sys.stdin.readline

d = int(input())
consult = [[-1, -1]]
for _ in range(d):
    day, pay = map(int, input().split())
    consult.append([day, pay])

DP = [0 for _ in range(d+1)]      # k 일까지 상담을 진행했을 때 얻을 수 있는 최대이익
for i in range(1, d+1):
    for j in range(1, i):
        if j + consult[j][0] <= i:
            DP[i] = max(DP[i], DP[j])
    
    if i + consult[i][0] <= d+1:
        DP[i] += consult[i][1]

print(max(DP))


# 2. 퇴사2 15486 - 실버 1
import sys
input = sys.stdin.readline

consult = {}
n = int(input())
for i in range(n):
    consult[i] = list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(0, n):
    if i + consult[i][0] <= n:
        dp[i + consult[i][0]] = max(dp[i + consult[i][0]], dp[i] + consult[i][1])

    dp[i+1] = max(dp[i+1], dp[i])       

print(dp[n])