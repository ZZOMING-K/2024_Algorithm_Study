import time

N = int(input())
rgb = []
priority1 = []
priority2 = []

locSmall = []
locMid = []
locBig = []


for i in range(N):
    rgb.append(list(map(int, input().split())))
    big = max(rgb[i])
    small = min(rgb[i])
    for j in range(3):
        if j == 2 or (rgb[i][j] != big and rgb[i][j] != small):
            mid = rgb[i][j]
            break
    if big == small:
        locSmall.append(0)
        locMid.append(1)
        locBig.append(2)
    else:
        for j in range(3):
            if rgb[i][j] == small:
                locSmall.append(j)
                break
        for j in range(3):
            if rgb[i][j] == big:
                locBig.append(j)
                break
        for j in range(3):
            if j != locSmall[i] and j != locBig[i]:
                locMid.append(j)
                break
        
    
    priority1.append([i, rgb[i][locBig[i]] - rgb[i][locMid[i]]])
    priority2.append([i, rgb[i][locMid[i]] - rgb[i][locSmall[i]]])

'''
for i in range(N):
    print(rgb[i])
    print(locSmall[i], locMid[i], locBig[i])
'''


priority1.sort(key = lambda x:x[1])
priority2.sort(key = lambda x:x[1])
'''
print(priority1)
print(priority2)
print()
'''
answer = [-1 for i in range(N)]

now1 = priority1.pop()
now2 = priority2.pop()


while priority1 and priority2:
    '''
    print(now1)
    print(now2)    
    print(answer)
    print()
    time.sleep(0.5)
    '''
    
    if answer[now1[0]] != -1:
        if priority1:
            now1 = priority1.pop()
            continue
    if answer[now2[0]] != -1:
        if priority2:
            now2 = priority2.pop()
            continue
    
    if now1[1] >= now2[1]:
        if now1[0] != N-1 and now1[0] != 0 and answer[now1[0] + 1] != -1 and answer[now1[0] - 1] != -1:
            answerList = [0, 1, 2]
            expt = []
            expt.append(answer[now1[0] + 1])
            expt.append(answer[now1[0] - 1])
            expt = list(set(expt))
            for i in expt:
                answerList.remove(i)
                
            if locSmall[now1[0]] in answerList:
                answer[now1[0]] = locSmall[now1[0]]
            elif locMid[now1[0]] in answerList:
                answer[now1[0]] = locMid[now1[0]]
            else:
                answer[now1[0]] = locBig[now1[0]]
            continue
            
        elif now1[0] != N-1 and answer[now1[0] + 1] != -1:
            if answer[now1[0] + 1] != locBig[now1[0]]:
                if answer[now1[0] + 1] == locSmall[now1[0]]:
                    answer[now1[0]] = locMid[now1[0]]
                else:
                    answer[now1[0]] = locSmall[now1[0]]

        elif now1[0] != 0 and answer[now1[0] - 1] != -1:
            if answer[now1[0] - 1] != locBig[now1[0]]:
                if answer[now1[0] - 1] == locSmall[now1[0]]:
                    answer[now1[0]] = locMid[now1[0]]
                else:
                    answer[now1[0]] = locSmall[now1[0]]
        if answer[now1[0]] != -1:
            continue
 
    if now2[0] != N-1 and now2[0] != 0 and answer[now2[0] + 1] != -1 and answer[now2[0] - 1] != -1:
            answerList = [0, 1, 2]
            expt = []
            expt.append(answer[now2[0] + 1])
            expt.append(answer[now2[0] - 1])
            expt = list(set(expt))
            for i in expt:
                answerList.remove(i)
                
            if locSmall[now2[0]] in answerList:
                answer[now2[0]] = locSmall[now2[0]]
            elif locMid[now2[0]] in answerList:
                answer[now2[0]] = locMid[now2[0]]
            else:
                answer[now2[0]] = locBig[now2[0]]
            continue

    
    elif now2[0] != N-1 and answer[now2[0] + 1] != -1:
        if answer[now2[0] + 1] == locSmall[now2[0]]:
            answer[now2[0]] = locMid[now2[0]]
        else:
            answer[now2[0]] = locSmall[now2[0]]
            
    elif now2[0] != 0 and answer[now2[0] - 1] != -1:
        if answer[now2[0] - 1] == locSmall[now2[0]]:
            answer[now2[0]] = locMid[now2[0]]
        else:
            answer[now2[0]] = locSmall[now2[0]]
    else:
        answer[now2[0]] = locSmall[now2[0]]


finalAns = 0
for i in range(N):
    if answer[i] == -1:
        if i != N - 1 and i != 0:
            answerList = [0, 1, 2]
            expt = []
            expt.append(answer[i + 1])
            expt.append(answer[i - 1])
            expt = list(set(expt))
            for j in expt:
                answerList.remove(j)
            
            if locSmall[i] in answerList:
                answer[i] = locSmall[i]
            elif locMid[i] in answerList:
                answer[i] = locMid[i]
            else:
                answer[i] = locBig[i]
                
        elif i == N-1:
            if answer[i - 1] == locSmall[i]:
                answer[i] = locMid[i]
            else:
                answer[i] = locSmall[i]
        elif i == 0:
            if answer[i + 1] == locSmall[i]:
                answer[i] = locMid[i]
            else:
                answer[i] = locSmall[i]
    #print(answer[i], rgb[i][answer[i]])
    finalAns = finalAns + rgb[i][answer[i]]
print(finalAns)
