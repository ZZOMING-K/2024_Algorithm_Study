#solution 아이디어 
#1. 전선을 끊은 뒤 인접노드의 개수 세기.
#1-1. 인접노드의 개수를 세는 건 bfs를 활용하여 노드 개수 check 
#1-2. 노드 개수 차이를 계산하여 가장 작은 수 return 


from collections import deque 

def solution(n, wires):
    
    def bfs(start , graph ,visited) : 
        queue = deque([start])
        visited[start] = True
        count = 0 
        
        while queue : #큐가 빌때까지 반복
            v  = queue.popleft()
            count+=1
            for i in graph[v] :
                if not visited[i] :
                    queue.append(i)
                    visited[i] = True 
        return count #노드를 방문할 때 마다 count 되기에 노드 개수를 알 수 있음. 
    
    graph = [[] for _ in range(n+1)] #graph 생성 
    
    for v1 , v2 in wires :
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    min_diff = float('inf') 
    
    for v1 , v2 in wires :
        graph[v1].remove(v2) #인접노드 삭제 (전선 끊기)
        graph[v2].remove(v1) 
        
        visited = [False] * (n+1) 
        
        #전선을 끊은 후 각 트리의 노드 수 계산 
        sub1_tree = bfs(v1,graph,visited) 
        sub2_tree = n - sub1_tree 
        diff_tree = abs(sub1_tree - sub2_tree) 
        min_diff = min(min_diff , diff_tree) 
        
        #끊었던 전선 다시 연결하기 
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return min_diff