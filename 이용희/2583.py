# 영역 구하기
# https://www.acmicpc.net/problem/2583

import sys
from collections import deque

input = sys.stdin.readline
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = -1

def bfs(i, j):
    area = 1
    q = deque()
    q.append((i, j))
    graph[i][j] = 1
    while q:
        i, j = q.popleft()
        for n in range(4):
            ni, nj = i + dir[n][0], j + dir[n][1]
            if ni < 0 or ni >= M or nj < 0 or nj >= N:
                continue
            if graph[ni][nj] == 0:
                q.append((ni, nj))
                area += 1
                graph[ni][nj] = 1
    return area

answer = []
count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            area = bfs(i, j)
            answer.append(area)
            count += 1
print(count)
print(*sorted(answer))