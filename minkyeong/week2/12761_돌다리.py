from collections import deque

# A,B,N,M 입력받기 
A, B, N, M = map(int, input().split())
graph = [-1]*100001 

def bfs(node):
    q = deque()
    q.append(node) #현재 위치 큐에 추가 
    graph[node] = 0 #현재 위치 방문 처리 
    while q: #큐가 빌때 까지 반복 
        node = q.popleft()  
        
        #현재 위치에서 움직일 수 있는 거리  
        for n in [node-1, node+1, node+A, node-A, node+B, node-B, node*A, node*B]:
            if (0 <= n <= 100000) and graph[n] == -1: #만일 이동할 위치가 100000 이하이고, 방문한 적이 없다면 큐에 추가 
                q.append(n)
                graph[n] = graph[node]+1 # 이동횟수 +1회 추가 
                if n == M: #M번 위치에 도달했을 때 멍춤 
                    break 

bfs(N) #BFS 함수 수행 
print(graph[M]) #최소한의 이동횟수 반환 