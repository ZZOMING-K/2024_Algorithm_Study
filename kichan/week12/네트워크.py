def bfs(n, computers, i, visited):
    visited[i] = 1
    q = []
    q.append(i)
    
    while q:
        now = q.pop(0)
        
        for j in range(n):
            if j != now and computers[now][j] == 1:
                if visited[j] == 0:
                    visited[j] = 1
                    q.append(j)
    

def solution(n, computers):
    answer = 0
    
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            bfs(n, computers, i, visited)
            answer += 1
    return answer
