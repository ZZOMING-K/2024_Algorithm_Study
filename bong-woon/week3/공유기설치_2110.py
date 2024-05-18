n, c = map(int, input().split())
home_location = [int(input()) for _ in range(n)]
home_location.sort()

start = 1 # 공유기의 거리가 가질 수 있는 최솟값
end = home_location[-1] - home_location[0] # 공유기의 거리가 가질 수 있는 최댓값


while start <= end:
    distance = (start + end) // 2 # 최적화할 공유기 사이의 거리
    set_home = home_location[0]
    count = 1
    for i in range(n):
        if home_location[i] - set_home >= distance:
            set_home = home_location[i]
            count += 1

    if count >= c:
        start = distance + 1

    else:
        end = distance - 1

print(distance)