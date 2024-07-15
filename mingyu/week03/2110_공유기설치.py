from bisect import bisect_left
import sys
input = sys.stdin.readline

N, C = map(int, input().split())

A = []
for i in range(N):
    A.append(int(input()))
A.sort()

minLength = 0
maxLength = A[-1] - A[0]

#print('Min Length : ', minLength, 'Max Length : ', maxLength)

answer = 0
sw = True
while sw:
    length = (maxLength + minLength) // 2
    if maxLength == minLength:
        sw = False
    
    #print('length : ', length, 'minLength : ', minLength, 'maxLength : ', maxLength)
    prev = A[0]         ##바로 직전의 공유기 위치가 저장될 변수, A[0]은 무조건 포함되므로 초기값으로 지정 가능
    cnt = C - 1         ##A[0]은 이미 포함되었으므로 C-1개의 공유기만 위치시키면 됨

    while cnt != 0:
        insertLocation = bisect_left(A, prev + length)
        if insertLocation < len(A) :     ##bisect_left로 이전집 + length 를 찾을 수 있는 경우
            #print('List : ', A)
            #print('prev : ', prev)
            #print('length : ', length)
            #print('insert location : ', insertLocation)
            #print('value : ', A[bisect_left(A, prev + length)])
            prev = A[insertLocation]
            cnt = cnt - 1
            
        else:
            #print('\nlength ', length, 'fail\n')
            maxLength = length - 1
            if maxLength < minLength:
                maxLength = length
            break

    if cnt == 0:
        #print('\nlength ', length, 'complete\n')
        minLength = length + 1
        answer = length

if answer == 0:
    print(A[1] - A[0])
else:
    print(answer)
