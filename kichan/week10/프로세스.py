from collections import deque

def solution(priorities, location):
    answer = 0

    pri = deque(priorities)
    nn = deque([i for i in range(len(priorities))])

    cnt = 0

    while pri:
        p = pri.popleft()
        n = nn.popleft()
        
        if len(pri)==0:
            return cnt+1

        if p >= max(pri):
            cnt += 1
            if n == location:
                return cnt
        else:
            pri.append(p)
            nn.append(n)