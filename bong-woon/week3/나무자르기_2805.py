n, m = map(int, input().split())
hl = [h for h in map(int, input().split())]

start = 0 # 나무가 가질 수 있는 최대 높이
end = max(hl) # 주어진 나무 중에서 최대 높이의 나무

cut_height = [] # 자르는 높이를 설정할 때마다 그 값을 저장할 리스트

while True:
    total = 0 # 상근이가 가지고 갈 나무
    mid = (start + end) // 2 # mid = 자르는 높이
    for h in hl: # 모든 나무에 댛서
        if h > mid: # 자르는 높이보다 큰 나무가 있다면 자르고 남은 길이를 total에 모두 더한다.
            total += (h - mid)
    
    if total >= m: # total을 계산하고 난 뒤 상근이의 목표량 m과 비교했을 때 m보다 크거나 같으면
        cut_height.append(mid) # 일단 조건에 만족하므로 설정 높이를 cut_height에 저장한다.
        start = mid + 1 # start 값을 새롭게 갱신해서 범위를 좁혀준다.
    else: # 상근이의 목표량 m에 도달하지 못한 경우 더 낮은 위치에서 잘라본다.
        end = mid - 1

    if start > end: # 검색을 반복하다가 start > end가 되면 종료
        break

print(max(cut_height)) # 잘라본 높이 중에서 최댓값을 출력