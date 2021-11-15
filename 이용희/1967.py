# 트리의 지름
# https://www.acmicpc.net/problem/1967

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(start):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    distance = [0] * (n + 1)
    while q:
        node = q.popleft()
        for next, cost in graph[node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                distance[next] = distance[node] + cost
    max_dist = max(distance)
    return max_dist, distance.index(max_dist)

dist, node = bfs(1)
answer, node = bfs(node)
print(answer)