import sys
sys.setrecursionlimit(10**6) # 백준에서 recursion error을 해결하기 위한 maximum recursion depth 설정

n = int(input()) # n 입력

map = [list([False] * n) for _ in range(n)] # n x n 크기의 RGB 값을 입력받을 2차원 리스트
check = [list([False] * n) for _ in range(n)] # n x n 크기의 방문 여부를 체크할 2차원 리스트

for i in range(n): # 행의 수만큼 반복하면서
    row = input() # 행 단위로 n개의 RGB 값을 입력
    for j, char in enumerate(row): # 하나의 행 안에 데이터를 돌면서,
        map[i][j] = char # i는 고정한 채 j만 바꾸면서 RGB 값을 입력받음 -> 하나의 행 완성

dx = [-1, 1, 0, 0] # 상하좌우 1칸씩 움직이기 위한 리스트
dy = [0, 0, -1, 1]

def dfs(x, y): # DFS
    if check[x][y] == True: # 방문 처리 되어있으면 아무것도 리턴하지 않음
        return
    else: # 방문 처리가 되어있지 않다면
        check[x][y] = True # 방문 처리를 해주고
        current_color = map[x][y] # current_color에 현재 RGB값 저장

        for k in range(4): # 상하좌우로 움직이기 위한 for문
            nx = x + dx[k] # nx, ny : 움직인 이후의 새로운 좌표값
            ny = y + dy[k] 

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1: # (0, 0)에서 (n-1, n-1)을 벗어나는 경우 다시 위로 올라가서 for문 진행(다음 스텝 확인)
                continue
            elif map[nx][ny] != current_color: # 현재 RGB 값과 이동하려고 하는 곳의 RGB 값이 다르면 다시 위로 올라가서 for문 진행(다음 스텝 확인)
                continue
            elif map[nx][ny] == current_color and check[nx][ny] == False: # 현재 RGB 값과 이동하려고 하는 곳의 RGB 값이 같고, 방문 처리가 되지 않은 곳이면
                dfs(nx, ny) # nx, ny로 다시 DFS
        return True

def dfs_rg(x, y): # 적록색약인 사람 기준의 DFS
    if check[x][y] == True:
        return
    else:
        check[x][y] = True
        current_color = map[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue
            elif map[nx][ny] != current_color: # 현재 RGB와 다음 위치의 RGB가 다른 경우 : 1.R-G  2.R-B  3.B-G -> 적록색약은 1번을 같은 색깔로 본다.
                if ((map[nx][ny] == 'R' and current_color == 'G') or (map[nx][ny] == 'G' and current_color == 'R')) and check[nx][ny] == False:
                    dfs_rg(nx, ny)
            elif map[nx][ny] == current_color and check[nx][ny] == False:
                dfs_rg(nx, ny)
        return True

count = 0
count_rg = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count += 1

check = [list([False] * n) for _ in range(n)] # dfs() 함수에서 방문처리된 check를 다시 초기화

for i in range(n):
    for j in range(n):
        if dfs_rg(i, j) == True:
            count_rg += 1

print(count, count_rg)