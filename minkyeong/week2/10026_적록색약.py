from collections import deque 

# N 입력받기 및 그래프 생성 
N = int(input())
graph = [list(input().strip()) for _ in range(N)] 


dx = [0,0,-1,1]
dy = [-1,1,0,0]

#bfs 함수 정의 
def bfs(y,x,visited, color) : 
    
    q = deque([(y,x)]) #현재 위치를 큐에 추가 
    visited[y][x] =  True # 현재 위치 방문 처리 
    
    while q : #큐가 빌때 까지 반복 
        y , x = q.popleft() #큐에서 원소 꺼내기 
        
        #상,하,좌,우 탐색 
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i] 
            
            #만일 그리드를 벗어나지 않고, 색깔이 동일하며 방문하지 않은 경우 큐에 추가 
            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == color and not visited[ny][nx]  :
                q.append((ny,nx))
                visited[ny][nx] = True  #방문처리 
                

# 구역 수 세기 
def count_color(graph):
    
    count = 0
    
    visited = [[False] * N for _ in range(N)] 
    
    #만일 방문하지 않은 경우 bfs 함수 실행 및 count 증가 
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, visited, graph[i][j])
                count += 1
    
    return count

#적록색약이 아닌 경우 출력 
normal = count_color(graph)
print(normal) 

#적록색약인 경우 graph에서 G를 R로 변경한 후 BFS 함수 수행  
graph = [['R' if color == 'G' else color for color in row] for row in graph]
color_blind = count_color(graph) 
print(color_blind)
