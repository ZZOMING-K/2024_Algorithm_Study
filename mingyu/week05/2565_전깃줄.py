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
            
