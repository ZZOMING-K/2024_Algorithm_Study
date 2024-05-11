from collections import deque

N , M , V = map(int, input().split()) 

graph = [[] for _ in range(N+1)]

for _ in range(M) : 
    a,b = map(int,input().split()) 

    graph[a].append(b)
    graph[b].append(a)

for connect in graph :
    connect.sort()

visited = [False] * len(graph)

def dfs(node) :

    visited[node] = True
    print(node , end = " ")
    
    for nxt in graph[node] :
        if visited[nxt] == True : 
            continue 
        dfs(nxt)

def bfs(node) :

    visited = [False] * len(graph) 

    q = deque([node])
    visited[node] = True

    while len(q) > 0 : 
        
        v = q.popleft()
        print(v , end = " ")
        
        for nxt in graph[v] : 
            if visited[nxt] == True : 
                continue
            q.append(nxt)
            visited[nxt] = True

dfs(V)
print()
bfs(V)