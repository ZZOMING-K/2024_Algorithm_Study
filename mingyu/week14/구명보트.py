def solution(people, limit):
    from collections import deque
    answer = 0
    people.sort()
    deq = deque()
    for i in people:
        deq.append(i)
    while deq:
        answer = answer + 1
        now = deq.pop()
        if deq:
            rest = deq.popleft()
            if now + rest > limit :
                deq.appendleft(rest)

    return answer
