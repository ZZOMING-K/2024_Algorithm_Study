import sys, heapq

n = int(input())       # sys.stdin.readline()
hp = []

for i in range(0,n):
    numbers = list(map(int, input().split()))

    if i == 0:
        for number in numbers:
            heapq.heappush(hp, number)
    else:
        for number in numbers:
            if number> hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, number)

print(heapq.heappop(hp))