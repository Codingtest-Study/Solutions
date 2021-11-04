# 지름길
# https://www.acmicpc.net/problem/1446

import sys
import heapq
input = sys.stdin.readline

n, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

distance = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)
    for start, end, length in graph:
        if i == start and end <= d and distance[end] > length + distance[i]:
            distance[end] = length + distance[i]

print(distance[d])