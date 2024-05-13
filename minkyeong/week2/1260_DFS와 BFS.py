from collections import deque 

#노드와 간선 개수, 탐색을 시작할 번호 입력 
N , M , V = map(int, input().split()) 

#그래프 생성 
graph = [[] for _ in range(N+1)]
 
for _ in range(M) : 
    a,b = map(int,input().split()) 

    graph[a].append(b)
    graph[b].append(a)

# 각 노드들을 오름차순으로 정렬 => 작은 번호의 노드부터 탐색 
for connect in graph :
    connect.sort()

#dfs 함수 정의 
def dfs(node) :
    
    visited = [False] * len(graph) #방문 체크 리스트 생성 

    visited[node] = True #탐색을 시작하는 노드 방문 처리 
    print(node , end = " ") #현재 노드 출력 
    
    for nxt in graph[node] : #해당 노드와 연결된 다른 노드 탐색 
        if visited[nxt] == True :  #만일 방문한 적이 있다면 무시, 아니라면 
            continue 
        dfs(nxt)

#bfs함수 정의 
def bfs(node) :

    visited = [False] * len(graph) #방문체크 리스트 생성 

    q = deque([node]) # 큐에서 노드 꺼내기 
    visited[node] = True #첫 노드 방문 처리 

    while len(q) > 0 :  #큐가 빌때까지 반복 
        
        v = q.popleft() 
        print(v , end = " ") #현재 노드 공백을 기준으로 출력 
        
        for nxt in graph[v] :  
            if visited[nxt] == True : #만일 방문했엇다면 무시  
                continue
            q.append(nxt) #방문 안했다면, 큐에 추가 및 방문 처리 
            visited[nxt] = True

dfs(V) #DFS 탐색 결과 출력 
print() 
bfs(V) #BFS 탐색 결과 출력 