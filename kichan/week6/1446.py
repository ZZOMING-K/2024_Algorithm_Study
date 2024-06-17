# 실패

import sys
input = sys.stdin.readline

N,D = map(int, input().split())

short = []

for _ in range(N):
    srt,end,dis = map(int, input().split())
    if (end < D) & ((end-srt)>dis):
        short.append([srt,end,dis])

shortcut = sorted(short, key=lambda x: (x[1], x[2]))

current_end = 0
result = 0
dp = [1] * (D+1)

for srt, end, dis in shortcut:
    if current_end <= srt:  # 현재 위치가 다음 시작점보다 작거나 같다면
        current_end = end   # 현재 위치 갱신
        result += dis       # 거리 누적 더해주기
        for i in range(srt, end):
            dp[i] = 0

print(result + sum(dp) - 1)