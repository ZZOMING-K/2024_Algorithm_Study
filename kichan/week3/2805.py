# 2805

import sys

n,m = map(int, sys.stdin.readline().split())            # 나무의 개수,집에 가져갈 나무의 길이
trees = list(map(int, sys.stdin.readline().split()))    # 나무들의 높이

low, high = 0, max(trees)       # 절단값의 최소,최대값
answer = 0

while low<=high:                
    result = 0
    mid = (low+high)//2         # 중간값

    for i in trees:
        if i > mid:
            result += i-mid     # 가져갈 수 있는 나무 높이 누적해서 더하기

    if result < m:              # 아직 모자르다면
        high = mid -1           # mid 값을 줄여줌과 동시에 가져갈 나무 증가
    else:                       
        answer = mid            # 초과로 잘랐다면
        low = mid + 1           # mid값을 늘려줌으로써 가져갈 나무 감소

print(answer)