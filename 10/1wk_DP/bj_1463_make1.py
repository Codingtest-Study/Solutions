# /2 , /3 , -1
# 그냥 할 수 있는 처리는 다 하고, 먼저 1에 도달하면 그 횟수를 출력

# DP Memoization 활용(Bottom-up)
# DP[k] 는 어차피 '상태' 에 대한 값이기 때문에 과정 상관 없이 최소값만 저장하면 된다.
import sys
input = sys.stdin.readline

n = int(input())
DP = [-1 for _ in range(n+1)]

for i in range(1, n+1):
    cnt = float('inf')
    if i%3 == 0:
        cnt = min(cnt, DP[i//3] + 1)
    if i%2 == 0:
        cnt = min(cnt, DP[i//2] + 1)
    cnt = min(cnt, DP[i-1] + 1)
    DP[i] = cnt

print(DP[n])



# deque 를 이용한 BFS 방식, popleft 과정에서 재정렬에 시간이 소요돼 시간초과가 나오는 거 같다.
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

tmps = deque([[n, 0]])

while tmps:
    cur_num, cur_cnt = tmps.popleft()
    if cur_num == 1:
        print(cur_cnt)
        sys.exit(0)
    nxt_cnt = cur_cnt + 1

    if cur_num%3 == 0:
        tmp3 = cur_num/3
        if tmp3 == 1:
            print(nxt_cnt)
            sys.exit(0)
        tmps.append([tmp3, nxt_cnt])

    if cur_num%2 == 0:
        tmp2 = cur_num/2
        if tmp2 == 1:
            print(nxt_cnt)
            sys.exit(0)
        tmps.append([tmp2, nxt_cnt])
    
    tmp1 = cur_num-1
    if tmp1 == 1:
        print(nxt_cnt)
        sys.exit(0)
    tmps.append([tmp1, nxt_cnt])

            
# 3으로 나눠지면 그냥 3으로 나눈 값만 넣으면 될 거 같았는데, 80%까지 정도 갔을 때 '틀렸습니다' 가 나왔다. (뭐지..?)
# 반례를 찾아보려 했는데, 반례는 모르겠고 cnt 수가 똑같은 경우는 6의 배수인 경우.