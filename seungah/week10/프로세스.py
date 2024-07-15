from collections import deque
def solution(priorities, location):
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    order = 0

    while queue:
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            order += 1
            if current[1] == location:
                return order

#많은 구글링의 결과로 실패 판단