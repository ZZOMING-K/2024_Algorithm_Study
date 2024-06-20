# ✍🏻 6주차 회고 

## 다익스트라 최단 경로

- **특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로 계산**
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작
    - 현실 세계의 도로(간선)은 음의 간선으로 표현되지 X

### 동작과정

1. 출발노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중에서 **`최단 거리가 가장 짧은 노드를 선택`** → **그리디 알고리즘** 
4. 해당 노드를 거쳐 다른 노드를 가는 비용을 계산하여 **`최단 거리 테이블 갱신`**
5. 3번과 4번 반복 


**[step1] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 1번 노드 처리** 

| 노드번호 | 1번 | 2번 | 3번 | 4번 | 5번 | 6번 |
| --- | --- | --- | --- | --- | --- | --- |
| 거리 | 무한 | 무한 | 무한 | 무한 | 무한 | 무한 |
| 거리 | 0(자기자신) | 2 | 5 | 1 | 무한  | 무한 |

**[step2] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 4번 노드 처리** 

| 노드번호 | 1번 | 2번 | 3번 | 4번 | 5번 | 6번 |
| --- | --- | --- | --- | --- | --- | --- |
| 거리 | 0(자기자신) | 2 | 5 | 1 | 무한 | 무한 |
| 거리 | 0(자기자신) | 2 | 4(갱신) | 1(결정)  | 2(갱신)  | 무한 |

**[step3] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 2번 노드 처리** 

| 노드번호 | 1번 | 2번 | 3번 | 4번 | 5번 | 6번 |
| --- | --- | --- | --- | --- | --- | --- |
| 거리 | 0(자기자신) | 2 | 5 | 1 | 무한 | 무한 |
| 거리 | 0(자기자신) | 2 | 4 | 1 | 2 | 무한 |

이미 방문처리된 노드라면 무시하는 방법 사용 가능 → 이미 최단거리 값이 결정되어 바뀌지 않기 때문이다. 

**[step4] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 5번 노드 처리** 

| 노드번호 | 1번 | 2번 | 3번 | 4번 | 5번 | 6번 |
| --- | --- | --- | --- | --- | --- | --- |
| 거리 | 0(자기자신) | 2 | 4 | 1 | 2 | 무한 |
| 거리 | 0(자기자신) | 2 | 3(갱신) | 1 | 2 | 4(갱신) |

**[step5~6] 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 3,6번 노드 처리** 

 **변화 X** 

| 노드번호 | 1번 | 2번 | 3번 | 4번 | 5번 | 6번 |
| --- | --- | --- | --- | --- | --- | --- |
| 거리 | 0 | 2 | 3 | 1 | 2 | 4 |

- 그리디 알고리즘 : **매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복**
- **단계를 거치며 한번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않는다.**

## 간단한 구현

- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차탐색)한다.

```python
import sys
input  = sys.stdin.readline
INF = int(1e9) #무한의미

n,m = map(int,input().split()) 
start = int(input()) 

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기 
graph =[[] for _ in range(n+1)] 

#방문한 적이 있는지 없는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1) 

#최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1) 

#모든 간선정보를 입력받기
for _ in range(m) :
	a,b,c = map(int,input().split()) 
	#a번 노드에서 b번 노드로 가는 비용이 c라는 의미
	graph[a].append((b,c)) 
	

#방문하지 않은 노드 중에서 가장 최단 거리가 짧은 번호를 반환 
def get_smallest_node() :
	min_value = INF 
	index = 0 
	for i in range(1 , n+1) :
	#만일 거리가 최단 거리보다 짧고 방문하지 않았다면, 최단거리 갱신 및 노드 갱신 
		if distance[i] < min_value and not visited[i] :
			min_value = distance[i] 
			index = i
	return index 

def dijksta(start) :
	#시작노드에 대해서 초기화
	distance[start] = 0
	visitde[start] = 0 
	
	for j in graph[start] :
		distance[j[0]] = j[1] 
	#시작노드를 제외한 전체 n-1개의 노드에 대해서 반복
	for i in range(n-1) :
		#현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리 
		now = get_smallest_node() 
		visited[now] = True 
		#현재 노드와 연결된 다른 노드 확인 
		for j in graph[now] : 
			cost = distance[now] + j[1] 
			# 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
			if cost < distance[j[0]] :
				distance[j[0]] = cost 
			

#다익스트라 알고리즘을 수행 
dijkstra(start) 

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1 , n+1) :
	#도달 할 수 없는 경우, 무한으로 출력 
	if distance[i] == INF :
		print("INF") 
	else: 
		print(distance[i]) 
		
```

## 우선순위 큐 (Priority Queue)

- 우선순위가 높은 데이터를 가장 먼저 삭제하는 자료구조 입니다.
- 예를 들어 여러개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우 이용

### 최소 힙

```python
import heapq 

#오름차순 힙 정렬
def heapsort(iterable) :
	h = [] 
	result = [] 
	#모든 원소를 차례대로 힙에 삽입
	for value in iterable :
		heapq.heappush(h , value) #특정 리스트에 데이터 넣을 때 사용 
		
	#힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
	for i in range(len(h)) :
		result.append(haepq.heappop(h)) #우선순위가 낮은 자료부터 나옴 
	return result
```

### 최대 힙

```python
import heapq 

#내림차순 힙 정렬
def heapsort(iterable) :
	h = [] 
	result = [] 
	#모든 원소를 차례대로 힙에 삽입
	for value in iterable :
		heapq.heappush(h , -value) #특정 리스트에 데이터 넣을 때 사용 
		
	#힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
	for i in range(len(h)) :
		result.append(-haepq.heappop(h)) #우선순위가 낮은 자료부터 나옴 
	return result	
```

## 다익스트라 알고리즘 : 개선된 구현 방법

→ 단계마다 방문하지 않은 노드에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙(Heap) 자료구조를 이용 

```python
import sys
input  = sys.stdin.readline
INF = int(1e9) #무한의미

n,m = map(int,input().split()) 
start = int(input()) 

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기 
graph =[[] for _ in range(n+1)] 

#최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1) 

#모든 간선정보를 입력받기
for _ in range(m) :
	a,b,c = map(int,input().split()) 
	#a번 노드에서 b번 노드로 가는 비용이 c라는 의미
	graph[a].append((b,c)) 
	
def dijkstra(start) :
	q = [] 
	
	#시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
	heapq.heappush( q , (0,  start)) 
	distance[start] = 0 
	
	while q: #q가 비어있지 않으면 
	#가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
	dist , now = heapq.heappop(q) 
	#현재 노드가 이미 처리된 적이 있는 노드라면 무시
	if distance[now] < dist :
		continue 
	#현재 노드와 연결된 다른 인접한 노드들을 확인
	for i in graph[now] :
		cost = dist + i[1] 
		#현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
		if cost < distance[i[0]] : 
			distance[i[0]] = cost
			heapq.heappush(q , (cost , i[0])) 
			
#다익스트라 알고리즘을 수행 
dijkstra(start) 

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1 , n+1) :
	#도달 할 수 없는 경우, 무한으로 출력 
	if distance[i] == INF :
		print("INF") 
	else: 
		print(distance[i]			
			
```

## 플로이드 워셜 알고리즘

**해당 알고리즘으로 6단계 법칙 풀이** 

- 모든 노드에서 다른 노드까지의 최단 경로를 모두 계산
- 플로이드 워셜 (Floyd-Warshall) 알고리즘은 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행
    - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않음
    - 시간복잡도가 $O(N^3)$  이다.
    - 노드 및 간선의 개수가 적은 경우에 잘 사용됨

각 단계마다 특정한 노드 K를 거쳐가는 경우를 확인

- `a에서 b로 가는 최단 거리`보다 `a에서 k를 거쳐 b`로 가는 거리가 더 짧은지 검사한다.

### 점화식

$$
 D_{ab} = min(D_{ab} , D_{ak} + D_{kb}) 
$$

| 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 1 | 0 | 4 | INF | 6 |
| 2 | 3 | 0 | 7 | INF |
| 3 | 5 | INF | 0 | 4 |
| 4 | INF | INF | 2 | 0 |

**[step1] 1번 노드를 거쳐 가는 경우를 고려하여 테이블 갱신** 


$D_{23} = min(D_{23} , D_{21} + D_{13})$ <br>
$D_{24} = min(D_{24} , D_{21} + D_{14})$  <br>
$D_{32} = min(D_{32} , D_{31} + D_{12})$  <br>
$D_{34} = min(D_{34} , D_{31} + D_{14})$  <br>
$D_{42} = min(D_{42} , D_{41} + D_{12})$  <br>
$D_{43} = min(D_{43} , D_{41} + D_{13})$  <br>

이후 2~4번 노드도 동일하게 테이블 갱신 

```python
INF = int(1e9) 

#노드의 개수 
n = int(input()) 
m = int(input()) 

#2차원 리스트를 만들고 , 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]] 

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 
for a in range(1, n+1) :
	for b in range(1, n+1) :
		if a==b :
			graph[a][b] = 0 

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m) :
	a,b,c = map(int, input().split())
	graph[a][b] = c 
	
#점화식에 따라 플로이드 워셜 알고리즘 수행 
for k in range(1, n+1) :
	for a in range(1, n+1) :
		for b in range(1 , n+1) :
			grpah[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b]) 
			
#수행된 결과를 출력 
for a in range(1,n+1) :
	for b in range(1,n+1) :
		if graph[a][b] == INF :
			print("INF") 
		else :
			print(graph[a][b]) 
```

✍🏻 **참고자료** 

[(이코테 2021 강의 몰아보기) 7. 최단 경로 알고리즘](https://youtu.be/acqm9mM1P6o?si=CnpsnuvQ9WQcP1ZA)

