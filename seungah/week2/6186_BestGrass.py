'''
6186
1. 열 R과 행 C를 입력
2. 웅덩이 위치를 입력
3. #를 찾는다
  1. #를 찾는다
  2. 위/아래/앞/뒤를 찾는다
  3. 있을시 하나로 친다
4. 개수 출력


'''

R, C = map(int, input().split())     #1


pasture = []
for i in range(R):                   #2
    pasture.append(list(map(str,input())))

found = []
for i in range(R):                   #3-1
    for j in range(C):
        if pasture[i][j] == '*':
            found.append((i, j))

around = [(0,1), (0,-1), (1,0), (-1,0)]
count = 0
for i in found:
    count += 1                     
    for j in around:                #3-2
        a = (i[0]+j[0], i[1]+j[1])
        if a in found:
            found.remove(a)         #3-3

print(count)                         #4
