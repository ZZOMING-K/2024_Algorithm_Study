import math

def solution(progresses, speeds):
    answer = []
    work = []
    n = len(progresses)
    
    for i in range(n):
        work.append(math.ceil((100-progresses[i]) / speeds[i]))
    
    idx = 0
    
    for j in range(n):
        if work[idx] < work[j]:
            answer.append(j-idx)
            idx = j
    
    answer.append(n-idx)
    
    return answer