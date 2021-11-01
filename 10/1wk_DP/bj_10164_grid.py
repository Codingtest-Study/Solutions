import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

if n == 1 or m == 1:
    print(1)
    sys.exit(0)

if k == 0 :         
    n1, m1, n2, m2 = n, m, 0, 0
else:
    if k%m == 0:            # 각 행의 마지막 열
        n1, m1 = k//m, m
    else: 
        n1, m1 = k//m + 1, k%m
    n2 = n - n1 +1
    m2 = m - m1 +1

def findPath(n, m):
    if n == m == 0:
        return 1
    if n ==1 or m == 1:
        return 1

    tot = n*m
    DP = [0 for _ in range(tot + 1)]
    DP[1] = 1

    for i in range(2, tot + 1):
        if i%m == 1:            # 각 행의 첫 번째 열
            DP[i] = DP[i-m]
        elif i//m == 0 or (i//m == 1 and i%m == 0):         # 첫 번째 행
            DP[i] = DP[i-1]
        else:
            DP[i] = DP[i-m] + DP[i-1]
    return DP[tot]

print(findPath(n1, m1)*findPath(n2, m2))
