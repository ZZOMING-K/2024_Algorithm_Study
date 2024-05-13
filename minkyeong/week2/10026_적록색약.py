from collections import deque 

N = int(input())
graph = [list(input().strip()) for _ in range(N)] 


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(y,x,visited, color) : 
    
    q = deque([(y,x)])
    visited[y][x] =  True
    
    while q : 
        y , x = q.popleft() 
        
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i] 
            
            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == color and not visited[ny][nx]  :
                q.append((ny,nx))
                visited[ny][nx] = True  
                

def count_color(graph):
    
    count = 0
    
    visited = [[False] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, visited, graph[i][j])
                count += 1
    
    return count


normal = count_color(graph)
print(normal) 

graph = [['R' if color == 'G' else color for color in row] for row in graph]
color_blind = count_color(graph) 
print(color_blind)
