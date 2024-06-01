#안 겹치는 전선끼리 배열을 만들어보자
#문제의 예제로 봤을 때
#1-8, 3-9, 10-10끼리 / 2-2, 6-4, 7-6, 9-7, 10-10끼리 / 4-1, 6-4, 7-6, 9-7, 10-10끼리
#아니면 그냥
#[[안 겹침] [한 개 겹침] [두 개 겹침] ... ] 이런식으로 해야되나?

#[[1, 8], [3, 9]] -> [[[3, 9]] [[1, 8], [2, 2]]] 이런식으로?
# 이게 나을듯?
# 1-8 3-9
# 3-9 // 1-8 2-2
# x // 3-9 // 1-8 2-2 // 4-1

#이럼안될듯?
#1-8 > 2-2, 4-1, 6-4, 7-6, 9-7
#3-9 > 4-1, 6-4, 7-6, 9-7
#2-2 > 1-8, 4-1
#4-1 > 1-8, 2-2, 3-9
#6-4 > 1-8, 3-9
#7-6 > 1-8, 3-9
#9-7 > 1-8, 3-9
#10-10

#이거를 행렬로 만들어보면
#XXOOOOOX
#XXXOOOOX
#OXXOXXXX
#OOOXXXXX
#OOXXXXXX
#OOXXXXXX
#OOXXXXXX
#XXXXXXXX

# -> 전부다 X로 만들어야 됨
#개수 센다음에 제일 많은 행을 X로 만들면서 반복해보자
#그러려면 몇 개 겹치는지 세는 배열도 필요함
#[5, 4, 2, 3, 2, 2, 2, 0]배열 필요
#선의 start, end를 저장하는 배열 필요

N = int(input())

numberOfCrossedLine = [[i, 0] for i in range(N)]      #겹치는 줄의 수
cross = [[] for i in range(N)]
matrix = []         #입력될 전깃줄들

for i in range(N):
    newLine = list(map(int, input().split()))
    for j in range(len(matrix)):
        if (matrix[j][0] > newLine[0] and matrix[j][1] < newLine[1]) or (matrix[j][0] < newLine[0] and matrix[j][1] > newLine[1]):
            numberOfCrossedLine[i][1] += 1
            numberOfCrossedLine[j][1] += 1
            cross[i].append(j)
            cross[j].append(i)
    matrix.append(newLine)

'''
for i in cross:
    print(i)
    
numberOfCrossedLine.sort(key = lambda x:x[1])
print(numberOfCrossedLine)
'''

###자르는 순서도 중요하다..
###내려가는애가 많은지 올라가는애가 많은지

answer = 0
for i in range(N):
    copy = [j[:]for j in numberOfCrossedLine]
    copy.sort(key = lambda x:x[1])
    #print(copy)
    
    cutlist = [0]
    crossedNum = 0
    
    cutlist[0], crossedNum = map(int, copy.pop())
    
    if crossedNum <= 0:
        break
    
    while copy and copy[-1][1] == crossedNum:
        cutlist.append(copy.pop()[0])

    goDown = 0
    goUp = 0
    downCut = cutlist[0]
    upCut = cutlist[0]
    
    for j in cutlist:       #내려가는지 올라가는지 고르기
        if matrix[j][0] - matrix[j][1] < 0:
            goDown = goDown + 1
            if downCut == cutlist[0]:
                downCut = j
        elif matrix[j][0] - matrix[j][1] > 0:
            goUp = goUp + 1
            if upCut == cutlist[0]:
                upCut = j
                
    if goDown > goUp:
        cut = downCut
    else:
        cut = upCut
    
    numberOfCrossedLine[cut] = [cut, 0]
    answer = answer + 1
    for j in cross[cut]:
        numberOfCrossedLine[j][1] -= 1

print(answer)
            
