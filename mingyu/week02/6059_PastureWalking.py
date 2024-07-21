from collections import deque

N, Q = map(int, input().split())
From = []
To = []
MAX = 10001

length = [[MAX for i in range(N + 1)] for j in range(N + 1)] #입력값이 저장될 배열
connected = [set() for i in range(N + 1)]

for i in range(N-1):
    a, b, l = map(int, input().split())
    length[a][b] = l
    length[b][a] = l
    connected[a].add(b)
    connected[b].add(a)

for i in range(Q):
    f, t = map(int, input().split())        #from, to
    nodeQueue = deque()
    costQueue = deque()
    visited = set()
    visited.add(f)
    now = f
    answer = 0
    while True:
        if t in connected[now]:
            print(answer + length[now][t])
            break
        else:
            for j in connected[now]:
                if j in visited:
                    continue
                else:
                    visited.add(j)
                    nodeQueue.append(j)
                    costQueue.append(answer + length[now][j])
            now = nodeQueue.popleft()
            answer = costQueue.popleft()




'''
잘못된 접근:


import sys
#import time
input = sys.stdin.readline

N, Q = map(int, input().split())

From = []
To = []
MAX = 10001

length = [[MAX for i in range(N + 1)] for j in range(N + 1)] #입력값이 저장될 배열
fix = [set() for i in range(N + 1)]
connected = [set()for i in range(N + 1)]

for i in range(N + 1):
    length[i][i] = 0
    connected[i].add(i)
    fix[i].add(i)

for i in range(N-1):
    a, b, l = map(int, input().split())
    length[a][b] = l
    length[b][a] = l
    connected[a].add(b)
    connected[b].add(a)

for i in range(Q):
    f, t = map(int, input().split())
    From.append(f)
    To.append(t)

#fix된게 있다면 그거 쓰면 됨 (1->4로 갈 때 1->2의 최소값 찾았고, 2fix4 있는 경우)
for e, i in enumerate(From):
    while True:
        if To[e] in fix[From[e]]:
            break
        storeMin = [MAX, 0]

        #최소값 찾는다.
        for j in connected[i]:
            for k in connected[j]:
                if i == k:
                    continue
                if k in fix[i]:
                    continue
                if storeMin[0] > length[j][k] + length[i][j] and j != k:
                    storeMin = [length[j][k] + length[i][j], k]

        minLen = storeMin[0]
        minLoc = storeMin[1]  #고정할 위치
        
        length[i][minLoc] = minLen
        length[minLoc][i] = minLen
        
        fix[i].add(minLoc)
        fix[minLoc].add(i)
        
        connected[i].add(minLoc)
        connected[minLoc].add(i)
        
        for j in fix[minLoc]:
            if length[i][j] > minLen + length[minLoc][j]:
                
                tempLen = minLen + length[minLoc][j]
                
                length[i][j] = tempLen
                length[j][i] = tempLen
                
                fix[i].add(j)
                fix[j].add(i)
                
                connected[i].add(j)
                connected[j].add(i)
        
for i in range(len(From)):
    print(length[From[i]][To[i]])
'''
