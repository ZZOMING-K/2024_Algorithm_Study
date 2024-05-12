# Best Grass

from collections import deque

r,c = map(int,input().split())  # r:행(row) , c: 열(column)
pasture = [list(input()) for _ in range(r)]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        pasture[x][y] = '.'

        for dr,dc in dir:
            nr, nc = x+dr, y+dc

            if (0 <= nr < r) and (0 <= nc < c) and (pasture[nr][nc] == '#'):
                pasture[nr][nc] = '.'
                q.append((nr,nc))

dir = [(0,1), (0,-1), (-1,0), (1,0)]    # 상,하,좌,우
cnt = 0

for i in range(r):
    for j in range(c):
        if pasture [i][j] == '#':
            bfs(i,j)
            cnt += 1
print(cnt)

