import sys
input = sys.stdin.readline

n = int(input())
nums = [-1]
nums += list(map(int, input().split()))

DP = [0 for _ in range(n+1)]     # i 번째 숫자까지 최장 수열의 길이

for i in range(1, n+1):
    for j in range(1, i):
        if nums[j] < nums[i]:
            DP[i] = max(DP[j]+1, DP[i])

print(max(DP) + 1)