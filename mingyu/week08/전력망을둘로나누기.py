def countfunc(arr, start):
    include = [start]
    stack = [start]
    while stack:
        now = stack.pop()
        for i in range(len(arr)):
            if now in arr[i]:
                if arr[i][0] not in include:
                    include.append(arr[i][0])
                    stack.append(arr[i][0])
                if arr[i][1] not in include:
                    include.append(arr[i][1])
                    stack.append(arr[i][1])
    #print(start, len(include))
    return len(include)
                

def solution(n, wires):
    wires.sort()
    answers = []
    for i in range(len(wires)):
        duplicated = [j[:] for j in wires]
        start = duplicated[i]
        duplicated = duplicated[:i] + duplicated[i+1:]
        #print(i)
        answers.append(abs(countfunc(duplicated, start[0]) - countfunc(duplicated, start[1])))
        if answers[-1] == 0:
            break
    answer = min(answers)
    return answer
