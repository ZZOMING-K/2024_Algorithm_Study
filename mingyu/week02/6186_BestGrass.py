R, C = map(int, input().split())
pasture = [input() for i in range(R)]

def isValid(y, x, R, C):
    if y >= 0 and x >= 0 and y < R and x < C:
        return True
    else:
        return False

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

isVisit = [[False for i in range(C)]for j in range(R)]

answer = 0

for y, row in enumerate(pasture):
    for x, target in enumerate(row):
        if pasture[y][x] == '#':
            if not isVisit[y][x]:
                isVisit[y][x] = True
                answer = answer + 1
            for i in range(4):
                if isValid(y+dy[i], x+dx[i], R, C):
                    if pasture[y+dy[i]][x+dx[i]] == '#':
                        isVisit[y+dy[i]][x+dx[i]] = True
print(answer)
                
