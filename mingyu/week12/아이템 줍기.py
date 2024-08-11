#테두리를 따라 그리는 문제인듯?
#x값이 가장 작은 사각형에서 시작하여 그림을 그려보자
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    tmp = 0
    rectangle.sort()
    now = rectangle[0]
    nowX = rectangle[0][0]
    nowY = rectangle[0][1]
    direction = 'r'
    
    findItem = False
    findCharacter = False
    
    tmp = 0
    while not findItem or nowX != rectangle[0][0] or nowY != rectangle[0][1]:
        #print(now, direction, nowX, nowY)

        if direction == 'r':
            nowX = nowX + 1
        elif direction == 'u':
            nowY = nowY + 1
        elif direction == 'l':
            nowX = nowX - 1
        elif direction == 'd':
            nowY = nowY - 1

        answer = answer + 1
        
        if (findItem and not findCharacter) or (not findItem and findCharacter):
            #print(f'check, {tmp}')
            tmp = tmp + 1
            
        if nowX == itemX and nowY == itemY:
            findItem = True
            
        if nowX == characterX and nowY == characterY:
            findCharacter = True
        
        for i, line in enumerate(rectangle):
            if line == now:
                continue
            if direction == 'r' or direction == 'l':
                if line[0] == nowX or line[2] == nowX:
                    if (line[1] < nowY and line[3] > nowY) or (line[1] > nowY and line[3] < nowY):
                        if direction == 'r':
                            direction = 'd'
                            now = rectangle[i]
                            break
                        if direction == 'l':
                            direction = 'u'
                            now = rectangle[i]
                            break
            if direction == 'u' or direction == 'd':
                if line[1] == nowY or line[3] == nowY:
                    if (line[0] < nowX and line[2] > nowX) or (line[0] > nowX and line[2] < nowX):
                        if direction == 'd':
                            direction = 'l'
                            now = rectangle[i]
                            break
                        if direction == 'u':
                            direction = 'r'
                            now = rectangle[i]
                            break
        if (nowX == now[0] or nowX == now[2]) and (nowY == now[1] or nowY == now[3]):
            if direction == 'r':
                direction = 'u'
            elif direction == 'u':
                direction = 'l'
            elif direction == 'l':
                direction = 'd'
            elif direction == 'd':
                direction = 'r'

    return min(tmp, answer - tmp)
