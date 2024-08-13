from collections import deque 
def solution(maps):
    
    #1은 벽이 없는 자리 
    def isValid(r,c) :
        return 0 <= r < row_len and 0 <= c < col_len and maps[r][c] == 1 
    
        
    row_len , col_len = len(maps) , len(maps[0])
    visited = [[False] * col_len for _ in range(row_len)]
    
    # 동 , 서, 남,  북 
    dr = [0 , 0  , 1 , -1]
    dc = [1 , -1  , 0 , 0]
    
    def bfs(r,c) :
        q = deque([(r,c,1)])
        visited[r][c] = True
        
        while q : #큐가 빌때까지 반복 
            r , c , dist = q.popleft() 
   
            if (r == (row_len-1)) and (c == (col_len-1)) : #마지막 지점에 도달 했을 경우  
                return dist 
            
            for i in range(4) :
                next_r = r + dr[i]
                next_c = c + dc[i] 
            
                if isValid(next_r , next_c) :
                    if not visited[next_r][next_c] :
                        q.append((next_r, next_c, dist+1))
                        visited[next_r][next_c] = True 
        return -1 
    
    return bfs(0,0)
    