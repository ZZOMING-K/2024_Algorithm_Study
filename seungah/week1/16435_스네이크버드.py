'''
Q:16435
1. 1열에 과일의 개수 N, 스네이크버드 초기 길이 L 입력
2. 2열에 과일N개의 높이 h를 입력
3. 최대 길이 출력
    1. 과일을 먹을 수 있으면 과일을 먹고 성장 & 다음 열매 찾기
    2. 없으면 스톱 
    
=결과는 제대로 나오는데 백준에서는 틀리게 나옴...
'''

N, L = map(int, input().split())  #1

h = list(map(int, input().split()[:N]))  #2

def growth(L, h):  
    if L in h:
        return growth(L + 1, h)  #3-1
    else:
        return L  #3-2

print(growth(L, h))  #3

