from collections import deque

def bfs(st,ed,graph,visited):

    visited[st] = 1
    visited[ed] = 1
    
    q = deque()
    q.append(ed)

    cnt = 1
    
    while q:
        a = q.popleft()

        for b in graph[a]:
            if visited[b] == 0:
                visited[b] = 1
                cnt += 1
                q.append(b)

    return cnt

def solution(n, wires):
    
    answer = 101
    graph = [[] for _ in range(n+1)]
    
    for st, ed in wires:
        graph[st].append(ed)
        graph[ed].append(st)
        
    for st, ed in wires:
        visited = [0] * (n+1)
        res = bfs(st, ed, graph, visited)
        last = abs(n-res)
        ans = abs(res-last)
        answer = min(answer, ans)

    return answer