import heapq

n = int(input())
expt = n * 0.15
if expt % 1 < 0.5:
    expt = int(expt)
else:
    expt = int(expt) + 1

#print(expt)

heap = []

for i in range(n):
    heapq.heappush(heap, int(input()))

for i in range(expt):
    heapq.heappop(heap)

answer = 0

for i in range(n - (expt * 2)):
    answer = answer + heapq.heappop(heap)
    #print(answer)
if n == 0:
    print(answer)
else:
    answer = answer / (n - (expt * 2))
    if answer % 1 < 0.5:
        answer = int(answer)
    else:
        answer = int(answer) + 1
    print(answer)

###0.5에 round함수를 적용하면 0이 됨 >> 부정확
