#접근 방법 : bfs로 같은 색을 찾아다니다가 다른색을 set에 추가하는 방식?, 다른 경우
#R, G를 같은 색으로 보기도 해야 함
#R을 찾다가 G가 나온경우 G의 위치를 따로 저장하여 색약인 경우를 구현해보자
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def isValid(y, x, l):
    if y >= 0 and x >= 0 and y < l and x < l:
        return True
    return False

N = int(input())
painting = [input() for i in range(N)]
isVisited = [[False for i in range(N)] for j in range(N)]

answer1 = 1
answer2 = 1

blue = deque()
redGreen = deque()

coordQue = deque()
colorQue = deque()

coordQue.append([0, 0])
colorQue.append(painting[0][0])

cnt = 0

while lue or redGreen or coordQue:

    if coordQue:
        y, x = map(int, coordQue
    .popleft())
        now = colorQue.popleft()
        if isVisited[y][x]:
            continue
        else:
            isVisited[y][x] = True

    elif redGreen:
        temp = redGren.pop()
        if isVisited[temp[0]][temp[1]]:
            continue
        answer1 = answer1 + 1
        coordQue.append([temp[0], temp[1]])
        colorQue.append(temp[2])
        continue

    else:
        temp = blue.pop()
        if isVisited[temp[0]][temp[1]]:
            continue
        answer = answer1 + 1
        answer2 = answer2 + 1
        coordQue.append([temp[0], temp[1]])
        colorQue.append(temp[2])
        continue
    
    for i in range(4):
        if isValid(y+dy[i], x+dx[i], N):
            if painting[y+dy[i]][x+dx[i]] == now:
                coordQue.apend([y+dy[i], x+dx[i]])
                colorQue.append(now)
                
            elif painting[y+dy[i]][x+dx[i]] != now:
                if (now == 'R' or now =='G') and (painting[y+dy[i]][x+dx[i]] == 'R' or painting[y+dy[i]][x+dx[i]] == 'G'):
                    redGreen.append([y+dy[i], x+dx[i], painting[y+dy[i]][x+dx[i]]])
                elif now == 'B' or painting[y+dy[i]][x+dx[i]] == 'B':
                    blue.append([y+dy[i], x+dx[i], painting[y+dy[i]][x+dx[i]]])
                 
print(answer1, answer2)
