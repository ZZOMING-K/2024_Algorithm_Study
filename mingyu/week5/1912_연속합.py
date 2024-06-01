#10, -4, 3, 1, 5, 6, -35, 12, 21, -1
#10 6 -> 10보다 작아졌으니 버린다?
#-4 -> 10보다 작으니 버린다?
#3 1 5 6 -35 -> 3보다 작아졌으니 버린다?
#12 21 -1 33보다 작아졌으니 -1을 버린다?

#가능성이 있는애들만 더하면 됨
#10 -> 저장해야됨, 더 큰애가 나오면 버려야됨
#-4 저장안해도됨
#3 -> 저장해야됨
#3 + 1 -> 저장해야됨
#3 + 1 + 5 -> 저장해야됨
#3 + 1 + 5 + 6 -> 저장해야됨, 10보다 커졌으므로 10 버려야 됨
#3 + 1 + 5 + 6 -35 -> 저장하면 안됨
#12 -> 저장해야됨
#12 + 21 -> 저장해야됨, 15보다 커졌으므로 15 버려야됨
#12 + 21 - 1-> 저장하면 안됨

#저장할 변수 총 2개 (현재 위치가 포함된 수, 최대값을 저장한 수)
#음수가 나올때마다 갱신 --> 이러면 안됨
#음수가 나오면 정답을 갱신하고, subSum이 양수인 경우 그대로 진행해야됨

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
