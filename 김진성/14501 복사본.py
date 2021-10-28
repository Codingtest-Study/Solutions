# 일할 수 있는 시간
can_work_day = int(input())

# 상담 배정 배열
consultings = []

# 최대 수익
max_benefit = [0 for i in range(0, can_work_day)]

# 상담 예약 날짜를 2차원 배열로 형성
for i in range(0, can_work_day):
    consult = list(map(int, input().split( )))
    consultings.append(consult)

# def solution(x, y):
#     # 만약 상담 걸리는 시간 + 시작 날짜가 N보다 크면 실행할 수 없음
#     if (x + consultings[x][0]) > can_work_day:
#         return y
    
#     for i in range(x, can_work_day):
#         print(x, y + consultings[i][1])
#         if (i + consultings[i][0]) < can_work_day:
#             return solution(x + consultings[i][0], y + consultings[i][1])
#         elif (i + consultings[i][0]) == can_work_day:
#             return y + consultings[i][1]

# # j는 시작점을 말함
# for j in range(0, can_work_day):
#     benefit = solution(j, j, 0, 0)
#     max_benefit[j] = max(case_benefit[j])

# print(max(max_benefit))

from itertools import chain, combinations

# index 배열
index_array = [i for i in range(0, can_work_day)]

# 무작위 조합 생성
index_location = list(chain.from_iterable(combinations(index_array, i) for i in range(0, len(index_array)+1)))

max_value = 0

# 조합 배열에서 하나를 뽑아서 다른 걸 진행
for i in index_location:
    # 시간 초과 체크
    time_sum = 0

    # 간격 체크
    is_valid = True

    # 여기서의 max_value 함산
    value = 0

    # 길이가 1인 경우 그게 가장 큰 경우
    if len(i) == 1 and (consultings[i[0]][0] + i[0]) <= can_work_day:
        max_value = max(max_value, consultings[i[0]][1])
    # 길이가 1보다 큰 경우
    elif len(i) > 1:
        # 앞뒤 시간 간격 체크
        for j in range(0, len(i)):

            # 예를 들어, i = (0, 3)이면 3 + 0 > 다음 요소 이면 False 인데 다음 요소는 len(i)보다 작아야 한다. 간격이 맞아야 함
            if (j + 1) < len(i):
                if (consultings[i[j]][0] + i[j]) > i[j + 1]:
                    is_valid = False
                    break
            
            # 마지막 요소가 타임라인이 근무시간을 넘어가는 경우
            if (j + 1) == len(i):
                # 현재 위치 + 근무기간 : 9 + 1 = 10 
                if (consultings[i[j]][0] + i[j]) > can_work_day:
                    is_valid = False
                    break
                else:
                    is_valid = True
                    pass
            
            value += consultings[i[j]][1]
            
    # 모든 조건이 성립할 경우
    if is_valid:
        max_value = max(value, max_value)
    

print(max_value)
