from collections import deque

# n : 정점의 개수, m : 간선의 개수, v : 시작 정점의 번호
n, m, v = map(int, input().split())

# 어떤 노드끼리 연결되어 있는지 정보 입력
info  = [list(map(int, input().split())) for _ in range(m)]

# 방문 여부 확인하는 리스트
check = [False] * (n + 1)

# info 정보를 기반으로 노드 간의 연결 정보를 2차원 배열로 표시
# 2차원 배열로 표시하기 위한 빈 배열 생성
graph = [list() for _ in range(n + 1)]

# info와 노드 번호를 기반으로 graph에 값을 추가
# graph[1] = [2, 3]은 1번 노드와 연결된 노드는 2번, 3번이라는 의미
for i in range(1, n+1): # 노드 번호와
    for val in info: # info 리스트에 정보를 하나씩 돌면서
        if i in val: # 노드 번호가 info 리스트의 원소의 원소에 있다면
            for node in val: # info 리스트의 원소에 두 가지 정보 중에서
                if node != i: # 지금 체크하고 있는 노드 번호가 아닌 다른 숫자를
                    graph[i].append(node) # graph[노드번호]의 원소로 추가. graph[idx]도 리스트
                    
for val in graph:
    val.sort() # 작은 번호부터 방문하게 하기 위해 오름차순 정렬

def dfs(num, graph, check):
    check[num] = True
    print(num, end = ' ')
    for i in graph[num]:
        if check[i] == False:
            dfs(i, graph, check)

def bfs(num, graph, check):
    queue = deque([num])
    check[num] = True

    while queue:
        node_num = queue.popleft()
        print(node_num, end = ' ')
        for i in graph[node_num]:
            if check[i] == False:
                queue.append(i)
                check[i] = True

dfs(v, graph, check)
print('')
# check 초기화
check = [False] * (n + 1)
bfs(v, graph, check)