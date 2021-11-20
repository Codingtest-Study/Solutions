# 서버실
# https://www.acmicpc.net/problem/17245

import sys, math
input = sys.stdin.readline

computers = []
N = int(input())
total = 0
for _ in range(N):
    data = list(map(int, input().split()))
    computers.append(data)
    total += sum(data)

answer = 0
start = 0
end = 10000001
half = math.ceil(total / 2)
while start <= end:
    mid = (start + end) // 2
    now = 0
    for row in computers:
        for x in row:
            if x >= mid:
                now += mid
            else:
                now += x
    if now < half:
        start = mid + 1
    elif now >= half:
        end = mid - 1
        answer = mid
print(answer)