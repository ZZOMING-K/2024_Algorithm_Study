from collections import deque
N, M, V = map(int, input().split())
L = [[False for i in range(N+1)]for j in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    L[x][y] = True
    L[y][x] = True

def DFS(L, now):
    firstNode = now
    visitOrder = []
    stack = deque()
    stack.append(now)
    haveToBreak = False
    
    while True:
        if haveToBreak:
            break
        if now not in visitOrder:
            visitOrder.append(now)
        
        for index, isLinked in enumerate(L[now]):
            if isLinked and index not in visitOrder:
                now = index
                stack.append(now)
                break
            if index == len(L) - 1:
                if now == firstNode:
                    haveToBreak = True
                    break
                stack.pop()
                if stack:
                    now = stack[-1]
    for i in visitOrder:
        print(i, end = ' ')
    print()
   
def BFS(L, now):
    visitOrder = []
    queue = deque()
    queue.append(now)
    
    while queue:
        now = queue.popleft()
        visitOrder.append(now)
        for index, isLinked in enumerate(L[now]):
            if isLinked and index not in visitOrder and index not in queue:
                queue.append(index)
    for i in visitOrder:
        print(i, end = ' ')

DFS(L, V)
BFS(L, V)
