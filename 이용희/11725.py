# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

node = deque([1])
parent = [[0] for _ in range(n + 1)]

while node:
    now = node.popleft()
    for i in tree[now]:
        if not visited[i]:
            parent[i] = now
            node.append(i)
            visited[i] = True

for i in range(2, n + 1):
    print(parent[i])