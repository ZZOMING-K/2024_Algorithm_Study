# 3273 제출코드

n = int(input())
numbers = sorted(list(map(int, input().split())))
x = int(input())

left = 0
right = n-1
cnt = 0

while left < right:
    if numbers[left] + numbers[right] == x:
        cnt += 1

    if numbers[left] + numbers[right] < x:
        left += 1
    else:
        right -= 1

print(cnt)