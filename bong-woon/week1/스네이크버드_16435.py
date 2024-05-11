# 과일의 개수, 처음 스네이크 버드의 길이
n, l = map(int, input().split())

# 과일의 높이
hi = list(map(int, input().split()))

# 과일의 높이에 따라 오름차순 정렬
hi.sort()

for h in hi:
    if l >= h: # 먹을 수 있으면
        l += 1 # 길이가 1씩 증가

print(l)