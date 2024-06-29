#https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max1 = 0
    max2 = 0
    for i in sizes:
        if max1 < max(i[0], i[1]):
            max1 = max(i[0], i[1])
        if max2 < min(i[0], i[1]):
            max2 = min(i[0], i[1])
    answer = max1 * max2
    return answer

'''
미쳤다....

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

'''