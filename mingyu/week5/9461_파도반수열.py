#11122를 미리 저장해도 됨
#알아야 하는 정보 : 각 변의 길이 -> [1,1,2,2,3] -> [1,2,2,3,4] -> [2,2,3,4,5]
#규칙성을 발견했다 -> [1,1,2,2,3] 에서 popleft하고, leftshift하고, 마지막 원소와 더해서 append하면 될듯?
#N이 최대 100개이므로 전부 저장해놓아도 괜찮을듯?

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
