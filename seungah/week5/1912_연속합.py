'''N = int(input())
arr = list(map(int, input().split()))
sum = 0
totalsum = []
for i in arr:
    if i > -1:
        sum += i
    else:
        totalsum.append(sum)
        sum = 0

print(max(totalsum))

이후 카데인 알고리즘 발견
'''
N = int(input())
arr = list(map(int, input().split()))

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, N):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)