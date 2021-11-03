# 일방통행
# 1. 그냥 고속도로 도로 타고 자기 바로 직전 노드에서 오는 거
# 2. 지름길로 오는 경우
# 모든 도로상의 위치는 정수로 표현 됨.
# 그리디가 아님. 지름길이라고 무조건 선택 X (나중에 더 빠른 지름길이 나올 수도 있음)

import sys
from collections import defaultdict
from heapq import *
sys = sys.stdin.readline

n, d = map(int, input().split())
graph = defaultdict(list)          # 0~150, default : 자기 노드 + 1 과 연결되어 있음
for i in range(d):
    graph[i].append([i+1, 1])    # connected node, weight

for _ in range(n):
    s, e, l = map(int, input().split()) 
    if e <= d:
        graph[s].append([e, l])         # 지름길로 연결된 노드도 추가

mindist = [float('inf') for _ in range(d+1)]       # k 까지 도달하는 최소 거리
hq = []
heappush(hq, [0, 0])  # 현재 노드까지 오면서 누적된 wgt, node

while hq:
    cur_w, cur_n = heappop(hq)
    if mindist[cur_n] < cur_w: continue     # 더이상 작아질 수 없음
    
    for nxt_n, nxt_w in graph[cur_n]:
        dist = cur_w + nxt_w
        if mindist[nxt_n] > dist:
            mindist[nxt_n] = dist
            heappush(hq, [mindist[nxt_n], nxt_n])       # else : 이미 더 작은 거리로 힙큐에 들어가 있음

print(mindist[d])




