# 2110

import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))      # 집 개수 N, 공유기 C개
houses = [int(input()) for _ in range(n)]   # n개의 집 위치

houses.sort()

start = 1
end = houses[-1] - houses[0]              # 집사이 최대 길이
answer = 0

while (start<=end):
    mid = (start + end) // 2              # 이진 탐색을 위한 중간값
    cnt = 1                               # 공유기 갯수 
    machine = houses[0]                   # 첫번째 집에 공유기 설치

    for i in range(1,n):
        if houses[i] - machine >= mid:    # 집사이 최대 길이보다 크다면
            cnt += 1                      # 공유기 설치
            machine = houses[i]           # 마지막 공유기 설치위치 초기화

    if cnt >= c:            # 설치가 다 끝났을때,
        answer = mid        # 공유기를 정해진 갯수보다 많거나 같게 설치했다면
        start = mid + 1     # 최대길이 늘려주기(간격이 너무 좁은 것이 원인)

    else:
        end = mid-1         # 공유기가 모자라면
                            # 최대길이 즐여주기(간격이 너무 넓어서 모자람)
print(answer)