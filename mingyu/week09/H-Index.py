def solution(citations):
    citations.sort()
    length = len(citations)
    for i in range(length, -1, -1):
        if citations[-1 * i] >= i:
            return i
