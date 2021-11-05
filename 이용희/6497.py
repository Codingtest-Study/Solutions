# 전력난
# https://www.acmicpc.net/problem/6497

import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edges = []
    parent = [i for i in range(m)]
    answer = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))
        answer += z

    edges.sort(key=lambda x: x[2])
    for edge in edges:
        x, y, cost = edge
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
            answer -= cost
    print(answer)