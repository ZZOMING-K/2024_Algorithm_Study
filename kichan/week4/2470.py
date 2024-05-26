import sys

n = int(sys.stdin.readline())
squids = list(map(int, sys.stdin.readline().split()))

squids.sort()

result = abs(squids[0]+ squids[n-1])
pair = (squids[0], squids[n-1])

left = 0
right = n-1

while (left<right):
    current_sum = squids[left]+ squids[right]

    if abs(current_sum) < result:
        result = abs(current_sum)
        pair = (squids[left], squids[right])
        if result == 0:
            break

    if current_sum < 0:
        left += 1
    else:
        right -= 1

print(pair[0], pair[1])