#베이컨 6단계 법칙 
INF = int(1e9) 

#유저의 수 와 친구 관계의 수 입력받기 
N , M  = map(int,input().split())

graph = [[INF] * (N+1) for _ in range(N+1)]

#2차원 그래프 만들고 자기자신으로 가는 비용은 0으로 초기화 
for a in range(1,N+1) :
  for b in range(1,N+1) :
    if a == b : 
        graph[a][b] = 0    

for _ in range(M) :
    a,b = map(int,input().split()) 
    graph[a][b] = 1 #a에서 b로 가는 비용과 b에서 a로 가는 비용은 동일하다. 
    graph[b][a] = 1
  
for k in range(1, N+1) :
  for a in range(1, N+1) :
    for b in range(1, N+1) :
        graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b]) 
        graph[b][a] = graph[a][b]


result_sums = []

for row in graph :
    result_sums.append(sum(row[1:])) 

# 가장 작은 값
min_value = min(result_sums)
# 가장 작은 값을 갖는 인덱스를 구함 (index 메서드는 동일한 값이 여러개 있을 경우 최소값을 반환함) 
min_index = result_sums.index(min_value)
print(min_index)