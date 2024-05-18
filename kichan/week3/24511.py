# 24511

from collections import deque

n = int(input())                        # 자료구조의 개수
a = list(map(int, input().split()))     # 수열의 정보를 담은 리스트(0:큐, 1:스택)
b = list(map(int, input().split()))     # 길이 n의 수열 b
m = int(input())                        # 삽입할 수열의 길이
c = list(map(int, input().split()))     # 삽입할 원소를 담고 있는 수열 c

q = deque()

for i in range(n):
    if a[i] == 0:                       # 스택은 넣어봤자 바로 빼야하기 때문에
        q.append(b[i])                  # 큐인 b의 원소를 q에 삽입

for i in c:                             
    q.appendleft(i)                     # c의 원소를 하나씩 앞에서 넣어주고
    print(q.pop(), end=" ")             # pop을 해주면서 출력

'''
    a = [0,1,1,0]
    b = [1,2,3,4]
    c = [2,4,7]

    1. c의 원소가 하나씩, b의 0번째 인덱스부터 접근할 것인데
       큐라면, 원래 있던 b의 원소가 빠지고, 스택이면 들어가봤자 다시 나와야 하기 때문에,
       큐일 경우에, q에 추가해줌
    2. 스택인 원소는 어차피 불변. 신경쓰지 않고
       c의 원소를 하나씩 q의 왼쪽부터 채워주고 하나씩 pop 하면서 출력
'''