#지름길의 개수와 고속도로의 길이 정보 받아오기
N , D = map(int,input().split())
number_li = []
# 시작위치, 도착위치, 지름길의 길이 정보 받아오기
for _ in range(N) :
    start , end , cost = map(int,input().split())
    number_li.append([start, end , cost])

graph = [i for i in range(D+1)]

for i in range(D+1) :
    
    #지름길이랑 고속도로로 가는 길 중 작은 길 선택 
    graph[i] = min(graph[i] , graph[i-1]+1)

    for start , end , cost in number_li : #출발점 , 도착점 그리고 지름길로 갈 경우의 거리를 꺼내서 
        if i == start and end <= D : # 출발점에서 도착점까지 고속도로 길이와 지름길로 가는 경우를 비교해서 작은 수를 갱신 진행 
            graph[end] = min(graph[end] , graph[i] + cost) 

print(graph[D]) 