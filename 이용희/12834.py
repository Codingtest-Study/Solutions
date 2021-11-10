# 주간 미팅
# https://www.acmicpc.net/problem/12834

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, v, e = map(int, input().split())
A, B = map(int, input().split())
house = list(map(int, input().split()))

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, i = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

def dijkstra(start):
    q = []
    distances[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distances

result = 0

for h in house:
    distances = [INF] * (v + 1)
    dijkstra(h)

    if distances[A] == INF:
        result += -1
    else:
        result += distances[A]

    if distances[B] == INF:
        result += -1
    else:
        result += distances[B]

print(result)