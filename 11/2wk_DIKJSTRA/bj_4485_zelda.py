import sys
input = sys.stdin.readline
from heapq import *

def solve(n, cost_map):
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]         # 모든 좌표는 (r, c)
    min_cost = [[float('inf') for _ in range(n)] for _ in range(n)]     # (k, l) 까지 이동하는 데 걸린 최소 cost
    hq = []
    heappush(hq, [cost_map[0][0], (0, 0)] )      
    while hq:
        c_cost, (c_r, c_c) = heappop(hq)
        for d in dirs:
            n_r, n_c = c_r + d[0], c_c + d[1]
            if 0 <= n_r < n and 0 <= n_c < n and min_cost[n_r][n_c] > c_cost:
                n_cost = c_cost + cost_map[n_r][n_c]
                if min_cost[n_r][n_c] > n_cost:
                    min_cost[n_r][n_c] = n_cost
                    heappush(hq, [n_cost, (n_r, n_c)])

    return min_cost[-1][-1]

caves = []
while True:
    try:
        n = int(input())
        if n == 0: break
        caves.append([list(map(int, input().split())) for _ in range(n)])
        print("Problem {}: {}".format(len(caves), solve(n, caves[-1])))
    except:
        break
