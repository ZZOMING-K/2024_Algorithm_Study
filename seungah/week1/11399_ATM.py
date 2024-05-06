'''
Q:11399
1. 줄을 서는 사람 수 N 입력
2. 사람 N이 각각 인출할때 걸리는 시간 P 입력
3. 시간의 합의 최솟값 출력
    1. 오름차순 정렬
    2. 각 사람이 걸리는 시간 계산
    3. 시간의 합 계산
'''
N = int(input())  #1
P = list(map(int, input().split()))[:N]  #2
P = sorted(P)  #3-1
total = 0
total_all = 0
for i in P:
    total += i  #3-2
    total_all += total  #3-3

print(total_all)  #3
