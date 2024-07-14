def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    release = 0
    
    while progresses:
        if progresses[-1] >= 100:
            release = release + 1
            progresses.pop()
            continue
        if release >= 1:
            answer.append(release)
            release = 0
            continue
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
    if release >= 1:
        answer.append(release)
    return answer
