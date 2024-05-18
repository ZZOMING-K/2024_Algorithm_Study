# 프린터 큐
from collections import deque

t = int(input())    # t: 반복 횟수

for i in range(t):
    n, m = map(int, input().split())        # n:문서의 개수, m:궁금한 문서의 위치  
    q = deque(map(int, input().split()))    # q:문서의 중요도

    cnt = 0                                 # 인쇄한 횟수
    index = [i for i in range(n)]           # 각 문서의 위치(?) 고유 위치값(?)

    while q:
        if q[0] == max(q):                  # 맨 앞의 문서가 가장 중요하다면
            cnt += 1                        # 인쇄하자 (횟수+1)

            if index[0] == m:               # 내가 궁금한 문서의 위치랑 같은 문서라면
                print(cnt)                  # 인쇄 횟수 출력하고 종료
                break                       # (동일한 중요도의 문서 구분)

            else:
                q.popleft()                 # 인쇄했으니 q에서 제거
                del index[0]                # index도 q와 같이 움직이기

        elif q[0] < max(q):                 # 현재 중요도가 가장 중요한것이 아니라면
            q.append(q.popleft())           # 뒤로 보내기
            index.append(index[0])          # index도 q와 같이 움직이기
            del index[0]