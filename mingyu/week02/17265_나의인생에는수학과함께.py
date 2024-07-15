#접근 : 모든 경우의 수에 대해 저장하고, min max로 출력해보자
from collections import deque

def isValid(y, x, l):
    if y >= 0 and x >= 0 and y < l and x < l:
        return True
    else:
        return False
    
def calc(queue):
    result = []
    for i in queue:
        tempResult = 0
        tempSymb = '+'
        for j in i:
            if j.isdigit():
                if tempSymb == '+':
                    tempResult = tempResult + int(j)
                elif tempSymb== '-':
                    tempResult = tempResult - int(j)
                elif tempSymb == '*':
                    tempResult = tempResult * int(j)
            else:
                tempSymb = j
        result.append(tempResult)
    return result

dy = [0, 1]
dx = [1, 0]         #오른쪽 먼저

N = int(input())
board = [input().split() for i in range(N)]

coordQueue = deque()
exprsQueue = deque()
#스택에는 0,0 5-> 0,1 5+/ 1,0 5*-> 0,2 5+5/ 1,1 5+3/ 1,0 5*... 순서대로 들어가야 한다

coordQueue.append([0, 0])
exprsQueue.append(board[0][0])

while True:
    y, x = map(int, coordQueue.popleft())
    expression = exprsQueue.popleft()
    if y == N - 1 and x == N - 1:
        exprsQueue.append(expression)
        break
    for i in range(2):
        if isValid(y + dy[i], x + dx[i], N):
            coordQueue.append([y + dy[i], x + dx[i]])
            exprsQueue.append(expression + board[y + dy[i]][x + dx[i]])

result = calc(exprsQueue)
print(max(result), min(result))
