import heapq

N = int(input())

heap = []

for i in range(N):
    tmp = list(map(int, input().split()))
    tmp[0] = tmp[0] * -1
    tmp[1] = tmp[1] * -1
    heapq.heappush(heap, tmp)

laststart = 2 ** 31 * -1
answer = 0

while heap:
    start, end = list(map(int, heapq.heappop(heap)))
    #print(start, end)
    if end >= laststart:
        laststart = start
        answer = answer + 1
        #print('selected : ', start * -1, end * -1)
print(answer)
