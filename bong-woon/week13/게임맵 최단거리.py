from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(maps, x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
        return maps[n - 1][m - 1]
    
    
    if bfs(maps, 0, 0) != 1:
        answer = bfs(maps, 0, 0)
    else:
        answer = -1
        
    return answer