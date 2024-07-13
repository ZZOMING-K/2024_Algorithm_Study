'''

def solution(progresses, speeds):
    answer = []
    dist = []
    for i in range(len(speeds)):
        percentleft = 100 - progresses[i]
        timeleft = percentleft // speeds[i]
        answer.append(timeleft)
    
    max_time = answer[0]
    count = 1
    
    for i in range(1, len(speeds)):
        if answer[i] <= max_time:
            count += 1
        else:
            dist.append(count)
            max_time = answer[i]
            count = 1
    
    dist.append(count)
    
    return dist

마지막 테스트 케이스에서 틀림: // 에서 정확하게 계산이 안됨
'''


import math
def solution(progresses, speeds):
    answer = []
    dist = []
    for i in range(len(speeds)):
        percentleft = 100 - progresses[i]
        timeleft = math.ceil(percentleft / speeds[i])
        answer.append(timeleft)
    
    max_time = answer[0]
    count = 1
    
    for i in range(1, len(speeds)):
        if answer[i] <= max_time:
            count += 1
        else:
            dist.append(count)
            max_time = answer[i]
            count = 1
    
    dist.append(count)
    
    return dist