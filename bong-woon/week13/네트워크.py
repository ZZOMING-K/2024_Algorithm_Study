from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(start_v, computers):
        q = deque()
        q.append(start_v)
        visited[start_v] = True
        
        while q:
            current_com = q.popleft()
            
            for i, next_com in enumerate(computers[current_com]):
                if next_com == 1 and visited[i] == False: # 다음 컴퓨터와 연결되어 있고 방문하지 않은 경우
                    q.append(i) # next_com의 인덱스 값으로 방문 예약
                    visited[i] = True
        
    for i in range(n):
        if visited[i] == False:
            bfs(i, computers)
            answer += 1       

    return answer