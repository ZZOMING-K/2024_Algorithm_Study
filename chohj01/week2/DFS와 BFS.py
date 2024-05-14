from collections import deque

dfs_result = []
bfs_result = []
graph = dict()

g, v, start = map(int, input().split())

def graph_in(a, b, graph):
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = []
        graph[a].append(b)
    graph[a].sort()
    return graph

for i in range(v):
    a, b = map(int, input().split())
    graph = graph_in(a, b, graph)
    graph = graph_in(b, a, graph)
    
def dfs(graph, v, visited):
    visited[v] = True
    dfs_result.append(str(v))
    try:
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)
    except:
        pass

visited_dfs = [False] * (int(g)+1)
dfs(graph, start, visited_dfs)
print(" ".join(dfs_result))

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        ver = queue.popleft()
        bfs_result.append(str(ver))
        try:
            for i in graph[ver]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        except:
            pass
visited_bfs = [False]*(int(g)+1)
bfs(graph, start, visited_bfs)
print(" ".join(bfs_result))