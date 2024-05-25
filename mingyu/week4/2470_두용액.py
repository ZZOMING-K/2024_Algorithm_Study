from bisect import bisect_left

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

zeroIdx = bisect_left(solutions, 0)         #zeroIdx 부터 배열의 마지막까지 양수
#zeroIdx가 len(solutions)라면 배열의 모든 원소가 음수 -> 배열 맨 뒤 두개를 출력하면 됨
#zeroIdx가 0이라면 배열의 가장 작은 원소가 양수 -> 배열 맨 앞 두개를 출력하면 됨

minPositiveSum = 2000000000
minNegativeSum = 2000000000

if zeroIdx < len(solutions) - 1 :       #0보다 큰 원소가 두 개 이상인 경우
    minPositiveSum = solutions[zeroIdx] + solutions[zeroIdx + 1]        #가장 작은 양수 두개의 합
if zeroIdx > 1:                         #0보다 작은 원소가 두 개 이상인 경우
    minNegativeSum = (solutions[zeroIdx - 1] + solutions[zeroIdx - 2]) * -1     #가장 큰 음수 두개의 합

    
#zeroIdx가 len(solutions)라면 배열의 모든 원소가 음수 -> 배열 맨 뒤 두개를 출력하면 됨
#zeroIdx가 0이라면 배열의 가장 작은 원소가 양수 -> 배열 맨 앞 두개를 출력하면 됨
if zeroIdx == 0:
    print(solutions[0], solutions[1])
elif zeroIdx == len(solutions):
    print(solutions[-2], solutions[-1])
    
else:       #양수, 음수가 하나 이상씩 존재하는경우
    tmpSum = 2000000000                 #양수와 음수의 합들 중 최소값을 저장할 변수
    for i in range(zeroIdx):            #모든 음수에 대해 더해서 가장 0에 가까워지는 양수를 찾는다
        target = solutions[i] * -1
        targetIdx = bisect_left(solutions, target)
        if targetIdx < len(solutions):
            if abs(solutions[i] + solutions[targetIdx]) < tmpSum:
                tmpSum = abs(solutions[i] + solutions[targetIdx])
                tmpIdx = [i, targetIdx]
        if targetIdx > zeroIdx:
            if abs(solutions[i] + solutions[targetIdx - 1]) < tmpSum:
                tmpSum = abs(solutions[i] + solutions[targetIdx - 1])
                tmpIdx = [i, targetIdx - 1]

    if minPositiveSum <= minNegativeSum and minPositiveSum <= tmpSum:
        print(solutions[zeroIdx], solutions[zeroIdx + 1])
    elif minNegativeSum <= minPositiveSum and minNegativeSum <= tmpSum:
        print(solutions[zeroIdx - 2], solutions[zeroIdx - 1])
    else:
        print(solutions[tmpIdx[0]], solutions[tmpIdx[1]])