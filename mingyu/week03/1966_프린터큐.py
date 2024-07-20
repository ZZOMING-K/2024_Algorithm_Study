from collections import deque
import heapq

numOfTestcase = int(input())

for i in range(numOfTestcase):
    N, M = map(int, input().split())
    Importance = list(map(int, input().split()))
    deq = deque()                       ##우선순위에 따라 출력될 문서 목록
    heap = []                           ##우선순위가 저장된 힙 큐
    
    for j in range(N):
        poped = Importance.pop()
        heapq.heappush(heap, poped * -1)
        
        if j == N - M - 1:
            deq.appendleft([poped, True])
        else:
            deq.appendleft([poped, False])
    
    #print('\ndeq : ', deq)
    #print('priority queue : ', heap)
    answer = 1


    priority = heapq.heappop(heap) * -1     ##우선순위
    #print('first priority : ', priority)
    
    while True:
        poped = deq.popleft()
        
        if poped[0] == priority:        ##현재 우선순위에 맞는 문서인경우 출력해야함
            if poped[1] == True:        ##출력되는 문서가 타겟문서인경우 몇번째로 출력되었는지 print하고, 종료함
                print(answer)
                break
            else:                       ##출력되는 문서가 타겟문서가 아닌 경우 타겟문서의 출력 순위를 1 늘리고, 반복함
                answer = answer + 1
                priority = heapq.heappop(heap) * -1
                #print('heap poped, next priority : ', priority)
        else:                           ##현재 우선순위에 맞지 않는 문서인 경우 다시 큐의 맨 뒤로 보내야함
            deq.append(poped)
                
        
