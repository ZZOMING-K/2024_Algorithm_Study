'''
Q:1439
1. 문자열 S를 입력
2. 최소 횟수 출력
    1. 1->0나 0->1로 바뀌는 구간 감지
    2. 1로 혹은 0으로 뒤집을때의 횟수 비교 후 출력
'''

S = input()
zero_all = S.split('1') 
count0 = 0
for i in zero_all:  #2-1
    if i != '':
        count0 += 1

one_all = S.split('0')  #2-1
count1 = 0
for i in one_all:
    if i != '':
        count1 += 1


print(min(count0, count1)) #2-2