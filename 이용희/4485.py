# 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485

import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra():
    q = []
    distances = [[INF] * n for _ in range(n)]
    heapq.heappush(q, (graph[0][0], 0, 0))
    graph[0][0] = 0

    while q:
        dist, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print("Problem {0}: {1}".format(problem, distances[x][y]))
            break
        for i in range(4):
            nx, ny = x + dir[i][0], y + dir[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distances[nx][ny]:
                distances[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

problem = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    dijkstra()
    problem += 1