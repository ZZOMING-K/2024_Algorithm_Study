from collections import deque

N, Q = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    A, B, L = map(int, input().split())
    graph[A].append((B, L))
    graph[B].append((A, L))

def bfs(start, target):
    visited = set()  # 방문한 노드를 저장할 집합으로 변경
    
    queue = deque([(start, 0)]) 

    while queue:
        node, distance = queue.popleft()
        if node == target:
            return distance 

        visited.add(node)  # 방문한 노드를 집합에 추가
        
        for n, l in graph[node]: 
            if n not in visited:
                queue.append((n, distance + l)) 

for _ in range(Q):
    start, target = map(int, input().split())
    print(bfs(start, target))