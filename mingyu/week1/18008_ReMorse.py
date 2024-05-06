import math

A = input()

toMorse = {}

#입력값에서 문장기호와 공백을 제거하고, 모든 문자를 대문자로 변환하기 위한 반복문
for i in A:
    if i == '?' or i == '!' or i == '.' or i == ',' or i == ' ':
        continue
    else:
        i = i.upper()
        toMorse[i] = toMorse.get(i, 0) + 1  #딕셔너리 형태로 어떤 문자가 몇 번 들어가 있는지 저장한다.

#문자가 등장한 횟수 내림차순으로 정렬한다.
toMorse = sorted(toMorse.items(), key = lambda x:x[1], reverse = True)

#다음글자는 3초, 글자의 dot와 dash사이는 1초
#dash 0개에서 전부dash해서 클때까지 반복

now = 1             #now : 문자를 모스화하여 걸리는 시간
numberOfCase = 1    #numberOfCase : now 시간으로 표현 가능한 모스부호 종류의 수
dashMax = 0         #dashMax : now 시간안에 쓸 수 있는 dash의 최대값
nextDash = 3        #nextDaxh : now가 nextDash와 같아지면 dashMax를 1 늘려야 함

answer = -3         #맨 처음 문자의 경우 문자사이의 공백인 3초가 들지 않으므로 -3부터 시작한다.

for i in toMorse:   #i[0] : 모스로 변환하고자 하는 문자, i[1] : 해당 문자가 등장한 횟수
    if numberOfCase == 0:
        now = now + 2   #늘어나는 시간의 최소 단위는 2초이다. 한 문자사이에서 기호를 구별하는데 걸리는 1초 + dot을 입력하는데 1초
        if now == nextDash:             #dash를 하나 늘릴 수 있는 시간이 된다면
            nextDash = nextDash + 4     #dash는 3초에서 시작하여 4초마다 하나씩 늘어날 수 있다. (3초일 때 : dash를 입력하는데 3초, 7초일 때 : dash를 입력하는데 3초 + 기호를 구별하는데 1초 + dash를 입력하는데 3초 ..)
            dashMax = dashMax + 1       #dash를 하나 늘린다.
        numberOfCase = 1                #now 시간에 표현 가능한 경우의 수를 구하기 위한 변수
        dotMax = now // 2 + 1           #now시간에 나올 수 있는 dot의 최대값 계산
        for j in range(1, dashMax + 1): #j : dash 개수
            numberOfCase = numberOfCase + math.comb(dotMax - j, j) #dash가 한 개일 때의 경우의 수 부터 미리 계산한 최대 개수일 때의 경우의 수 까지 더한다.

    
    numberOfCase = numberOfCase - 1     #now시간에 표현 가능한 모스부호의 종류에서 하나를 쓴다.
    answer = answer + (i[1] * now) + (i[1]) * 3     #해당 문자가 등장한 횟수 * 모스로 표현하는데 걸리는 시간 + 각 문자를 구분하는데 걸리는 시간 (3초 공백)
    

print(answer)
