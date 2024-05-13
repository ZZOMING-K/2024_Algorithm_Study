# Pasture Walking

from collections import deque

def dfs(current,target):

    visited[current] = 1

    if current == target:
        return 0
    
    for neighbor, length in graph[current]:
        if visited[neighbor] == 0:
            path_length = dfs(neighbor, target)

            if path_length >=0:
                return path_length + length
    
    return -1

N, Q = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    A, B, L = map(int, input().split())
    graph[A].append((B, L))
    graph[B].append((A, L))

for i in range(Q):
    p1, p2 = map(int, input().split())
    visited = [False] * (N + 1)
    print(dfs(p1, p2))