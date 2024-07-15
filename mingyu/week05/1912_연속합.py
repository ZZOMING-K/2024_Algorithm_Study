from collections import deque

N = int(input())
Arr = deque(list(map(int, input().split())))
answer = Arr[0]
subSum = Arr[0]

Arr.popleft()

for i in Arr:
    if i < 0:
        if answer <= subSum:
            answer = subSum
        subSum = subSum + i
        if subSum <= 0:
            if answer >= 0:
                subSum = 0
            else:
                subSum = i
    else:
        if subSum <= 0:
            subSum = 0
        subSum = subSum + i
if answer <= subSum:
    answer = subSum
print(answer)
