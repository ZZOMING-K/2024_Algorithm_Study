from collections import deque

A, B, N, M = map(int, input().split())
graph = [-1]*100001 

def bfs(node):
    q = deque()
    q.append(node)
    graph[node] = 0
    while q:
        node = q.popleft()
        for n in [node-1, node+1, node+A, node-A, node+B, node-B, node*A, node*B]:
            if (0 <= n <= 100000) and graph[n] == -1:
                q.append(n)
                graph[n] = graph[node]+1
                if n == M:
                    return ;

bfs(N)
print(graph[M])