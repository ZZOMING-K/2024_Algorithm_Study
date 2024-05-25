import heapq
N = int(input())

posNum = []
negNum = []

for i in map(int, input().split()):
    if i > 0:
        heapq.heappush(posNum, i)
    else:
        heapq.heappush(negNum, i * -1)

minPosSum = 99999999999999999999999
minNegSum = 99999999999999999999999
sameSignSUm = 999999999999999999999

if len(posNum) >= 2:
    minPosSum = posNum[0] + posNum[1]
    if len(posNum) >= 3:
        minPosSum = min(minPosSum, posNum[0] + posNum[2])

if len(negNum) >= 2:
    minNegSum = negNum[0] + negNum[1]
    if len(negNum) >= 3:
        minNegSum = min(minNegSum, negNum[0] + negNum[2])

if minPosSum < minNegSum:
    sameSignSum = minPosSum
else:
    sameSignSum = minNegSum

min_heap = []

findAnswer = False

for i in negNum:
    
    if findAnswer:
        break
    if posNum:
        start = 0
        end = len(posNum) - 1
        mid = (start + end) // 2
    else:
        mid = 0
        break

    while start <= end:

        if posNum[mid] == i:
            findAnswer = True
            heapq.heappush(min_heap, (0, i * -1, i))
            break

        elif posNum[mid] < i:
            start = mid + 1
            mid = (start + end) // 2

        else:
            end = mid - 1
            mid = (start + end) // 2
    #print(start, end, mid)
    #반복문 종료시, 0이되는 값을 찾은 게 아니라면 start가 end보다 1 큰 상태임
    if mid < len(posNum) - 1:
        heapq.heappush(min_heap, (abs(posNum[mid + 1] - i), i * -1, posNum[mid + 1]))
    if mid > 0:
        heapq.heappush(min_heap, (abs(posNum[mid - 1] - i), i * -1, posNum[mid - 1]))
    if posNum:
        heapq.heappush(min_heap, (abs(posNum[mid] - i), i * -1, posNum[mid]))
#print(min_heap)


if not posNum:
    if len(negNum) >= 3:
        if negNum[0] + negNum[1] > negNum[0] + negNum[2]:
            print(negNum[2] * -1, negNum[0])
        else:
            print(negNum[1] * -1, negNum[0] * -1)
    else:
        print(negNum[1] * -1, negNum[0] * -1)
        
elif not negNum:
    if len(posNum) >= 3:
        if posNum[0] + posNum[1] > posNum[0] + posNum[2]:
            print(posNum[0], posNum[2])
        else:
            print(posNum[0], posNum[1])
    else:
        print(posNum[0], posNum[1])
        
else:
    answer = heapq.heappop(min_heap)
    if answer[0] > sameSignSum:
        if sameSignSum == minPosSum:
            if len(posNum) >= 3:
                if posNum[0] + posNum[1] > posNum[0] + posNum[2]:
                    print(posNum[0], posNum[2])
                else:
                    print(posNum[0], posNum[1])
            else:
                print(posNum[0], posNum[1])
        else:
            if len(negNum) >= 3:
                if negNum[0] + negNum[1] > negNum[0] + negNum[2]:
                    print(negNum[2] * -1, negNum[0])
                else:
                    print(negNum[1] * -1, negNum[0] * -1)
            else:
                print(negNum[1] * -1, negNum[0] * -1)

    else:
        print(answer[1], answer[2])


    
