#이분탐색 라이브러리 활용 
from bisect import bisect_left 

def solution(citations):
    # 오름차순 정렬
    citations.sort()
    
    n = len(citations)
    start , end = 0 , n
    max_h = 0 #h값 초기화 
    
    while start <= end : 
        h = start + end // 2
        if h <= n - bisect_left(citations, h):
            max_h = max(max_h , h)
            start += 1 
        else :
            end -= 1 
    
    return max_h