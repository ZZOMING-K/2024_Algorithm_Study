
#1. 목초지 N , 목초지 간 거리 계산 요청 개수인  Q 입력받기 
#2. 그래프 생성할 때, 연결된 노드 간 길이도 같이 추가  
#3. 큐 생성 > 현재 노드에서 갈 수 있으며 방문한적이 없는 노드 와 거리 (이전 거리 + 현재 거리) 추가
#4. 만일 목적지에 왔을 경우 누적 거리 반환  


from collections import deque

N, Q = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(N + 1)]

#입력된노드 연결 정보를 그래프로 구성 
for _ in range(N - 1):
    A, B, L = map(int, input().split()) #각 노드에 연결된 노드와 거리 추가 
    graph[A].append((B, L))
    graph[B].append((A, L))
    
print(graph)
print(graph[1][0])

def bfs(start, target):

    visited = [False for _ in range(N+1)]  #방문 체크 리스트 생성 
    queue = deque([(start, 0)]) #탐색을 시작하는 노드와 거리 큐에 추가 

    while queue:

        node, distance = queue.popleft() #큐에서 노드와 거리 꺼내기 
        if node == target: #만일 목적지에 도달한 경우 거리 반환 
            return distance 

        for n, l in graph[node]: 
            if not visited[n]: #만일 방문한적 없는 노드일 경우 
                queue.append((n, distance + l)) #큐에 노드와 거리 추가 
                visited[n] = True #방문처리 
                
for _ in range(Q):
    start, target = map(int, input().split()) #출발지와 목적지 입력받기 
    
    print(bfs(start, target)) #bfs 함수를 이용하여 거리 반환 