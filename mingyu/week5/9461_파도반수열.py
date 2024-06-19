
from collections import deque

answer = [1, 1, 1, 2, 2]
spiral = deque()
spiral.append(1)
spiral.append(1)
spiral.append(1)
spiral.append(2)
spiral.append(2)
for i in range(5, 100):
    poped = spiral.popleft()
    apndNum = poped + spiral[-1]
    spiral.append(apndNum)
    answer.append(apndNum)
    
for i in range(int(input())):
    print(answer[int(input()) - 1])
