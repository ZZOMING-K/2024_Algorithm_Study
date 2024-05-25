from collections import deque

n = int(input())
an = [a for a in map(int, input().split())] # 0 : queue, 1 : stack
bn = [b for b in map(int, input().split())] # 몇 번 자료구조에 어떤 원소가 들어있는지

m = int(input())
push_ele = [p for p in map(int, input().split())]

if 0 not in an: # queue가 하나도 없는 경우에는
    for ele in push_ele: # 삽입할 원소들을 그대로 출력
        print(ele, end = ' ')

else: # 큐가 하나라도 있다면
    q = deque()
    for a, b in zip(an[::-1], bn[::-1]):
        if a == 0: # a = 0에 대해서만 하나의 큐에 추가(스택은 무시)
            q.append(b)

    for ele in push_ele: # 하나의 큐에 대해서 append와 popleft를 반복 
        q.append(ele)
        print(q.popleft(), end = ' ')