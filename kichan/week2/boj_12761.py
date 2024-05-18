# 돌다리

from collections import deque

def bfs(n):
    q = deque()
    q.append(n)

    visited[n] = 1  # 방문한 돌 위치
    cnt[n] = 0     # 방문 횟수

    while q:
        visit = q.popleft()

        if visit == m:
            return cnt[visit]
        
        for i in [visit+1, visit-1, visit+a, visit-a, visit+b, visit-b, visit*a, visit*b]:
            if 0<= i <= 100000 and visited[i] == -1:
                visited[i] = 1
                cnt[i] = cnt[visit] + 1
                q.append(i)

a,b,n,m = map(int, input().split())

visited = [-1]*100001     # 0~100000
cnt = [0]*100001

answer = bfs(n)
print(answer)