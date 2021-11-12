# 아기 상어
# https://www.acmicpc.net/problem/16236

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

size = 2
shark_x, shark_y = 0, 0
answer = 0
eat = 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            shark_x, shark_y = i, j
            array[i][j] = 0
            break

def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque([(shark_x, shark_y)])
    dist[shark_x][shark_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 상어의 크기보다 작거나 같을 때만 지나감
            if dist[nx][ny] == -1 and array[nx][ny] <= size:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = int(1e9)
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < size:
                # 먹을 수 있는 물고기 중 최단 거리
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    # 먹을 수 있는 물고기가 없을 때
    if min_dist == int(1e9):
        return None
    else:
        return x, y, min_dist

while True:
    result = find(bfs())
    if not result:
        print(answer)
        break
    x, y, dist = result
    shark_x, shark_y = x, y
    answer += dist
    array[shark_x][shark_y] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0