import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
jewel = []
backpack = []

for i in range(N):
    heapq.heappush(jewel, list(map(int, input().split())))
for i in range(K):
    heapq.heappush(backpack, int(input()))


answer = 0
leftJewel = []

while backpack:
    currBackpackSize = heapq.heappop(backpack)
    while True:
        if jewel:
            weight, value = map(int, heapq.heappop(jewel))
            if weight > currBackpackSize:               #종료조건 1 : 베낭보다 큰 무게 들어옴
                heapq.heappush(jewel, [weight, value])
                if leftJewel:
                    answer = answer + heapq.heappop(leftJewel) * -1
                break
            else:
                heapq.heappush(leftJewel, value * -1)
        else:
            if leftJewel:                               #종료조건 2 : jewel배열이 전부 leftJewel로 옮겨짐
                answer = answer + heapq.heappop(leftJewel) * -1
            break

print(answer)
