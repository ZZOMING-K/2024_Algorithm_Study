n, c = map(int, input().split())

map = [list([False] * c) for _ in range(n)]
check = [list([False] * c) for _ in range(n)]

for i in range(n):
    row = input()
    for j, char in enumerate(row):
        map[i][j] = char

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if check[x][y] == True: # 이미 방문했다면 아무것도 반환 x
        return              
    else:
        check[x][y] = True
        if map[x][y] == '#': # '#'인 경우에만 상하좌우 탐색
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx > n-1 or ny < 0 or ny > c-1: # 맵 밖으로 벗어날 때는 무시하고 다시 for문 진행
                    continue                                  
                elif map[nx][ny] == '#' and check[nx][ny] == False: # '#'이면서 방문하지 않은 곳이라면 nx, ny에서 dfs
                    dfs(nx, ny)                                     
            return True
                
count = 0
for i in range(n):
    for j in range(c):
        if dfs(i, j) == True:
            count += 1
print(count)