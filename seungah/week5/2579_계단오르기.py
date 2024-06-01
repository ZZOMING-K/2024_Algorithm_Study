'''
계단은 한 번에 1 or 2개 오를 수 있다.
연속된 세 개의 계단을 밟지 못함. 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
=> Index Error
'''
import sys
input= sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]


sum = [stairs[0], stairs[0] + stairs[1], max(stairs[0] + stairs[2], stairs[1] + stairs[2])]

'''sum.append(stairs[0])
sum.append(stairs[0] + stairs[1])
sum.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))'''

if N > 3:
    for i in range(3,N):
        sum.append(max(sum[i-2] + stairs[i], sum[i-3] + stairs[i-1] + stairs[i]))


print(sum[-1])