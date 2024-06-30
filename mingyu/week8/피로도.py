import itertools

def solution(k, dungeons):
    arr = [i for i in range(len(dungeons))]
    nPr = itertools.permutations(arr, len(dungeons))
    answer = 0
    for i in nPr:
        tired = k
        now = 0
        for j in range (len(i)):
            if tired < dungeons[i[j]][0]:
                break
            if tired - dungeons[i[j]][1] >= 0:
                tired = tired - dungeons[i[j]][1]
                now = now + 1
                if now > answer:
                    answer = now
                
    return answer
