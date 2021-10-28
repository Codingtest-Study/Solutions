num = int(input())
value = [0 for i in range(0, num + 1)]
value[1] = 0

for i in range(2, num+1):
    value[i] = value[i - 1] + 1
    if i % 2 == 0:
        value[i] = min(value[i], value[i//2] + 1)
    if i % 3 == 0:
        value[i] = min(value[i], value[i//3] + 1)

print(value[num])