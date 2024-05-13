from collections import deque 

R, C = map(int, input().split()) 
# 그래프 생성 
graph = [list(input()) for _ in range(R)] 

# 상하좌우 탐색 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# BFS
def bfs(y, x): 
    #현재 위치 큐에 추가 
    q = deque([(y, x)])
    
    #만일 '.' 일 경우 grass 가 아닌 공간 
    if graph[y][x] == '.':
        return False 
    
    #현재 위치를 기준으로 BFS 탐색 실시 
    while q:
        y, x = q.popleft() 

        #현재 위치 값을 '#' 에서 '.' 으로 변경 
        graph[y][x] = '.' 
        
        # 상하좌우 탐색 
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]

            #만일 범위를 벗어나지 않으면서 그 위치의 값이 '#'인 경우 
            if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == '#': 
                q.append((ny, nx))
    
    #하나의 grass가 만들어지는 공간을 모두 탐색한 경우 True 반환 
    return True 

cnt = 0 

for i in range(R): 
    for j in range(C):
        if bfs(i, j):
            cnt += 1 

print(cnt)