from collections import deque
A, B, N, M = map(int, input().split())

queue = deque()
queue.append([N, 0])

def isValid(now, A, B, i):
    if i == 0:
        return now - 1 >= 0
    elif i == 1:
        return now + 1 <= 100000
    elif i == 2:
        return now - A >= 0
    elif i == 3:
        return now + A <= 100000
    elif i == 4:
        return now - B >= 0
    elif i == 5:
        return now + B <= 100000
    elif i == 6:
        return now * A <= 100000
    elif i == 7:
        return now * B <= 100000

def calculate(now, A, B, i):
    case = {
        0: now - 1,
        1: now + 1,
        2: now - A,
        3: now + A,
        4: now - B,
        5: now + B,
        6: now * A,
        7: now * B
    }
    return case[i]

whileSw = True
visited = set()

while whileSw:
    now, answer = map(int, queue.popleft())
    for i in range(8):
        if isValid(now, A, B, i):
            value = calculate(now, A, B, i)
            if value == M:
                print(answer + 1)
                whileSw = False
                break
            if value in visited:
                continue
            visited.add(value)
            queue.append([value, answer + 1])
        
        
