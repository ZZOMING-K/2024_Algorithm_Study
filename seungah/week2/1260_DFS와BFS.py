'''
1260
1. 정점 개수 N, 간선 개수 M, 시작 노드 V 입력
2. 간선이 연결하는 두 정점 번호를 M번 입력
   1. 행렬 생성
3. DFS
4. BFS


'''


N, M, V = map(int, input().split())
graph = {}
for i in range(M):
    a, b = map(int, input().split())
    graph.update(a = b)
    
    '''graph[a].append(b)
    graph[b].append(a)'''

 

print(graph)
'''[ []*(N+1) for _ in range(N+1)]


for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
print(graph)

def dfs(graph, V)'''