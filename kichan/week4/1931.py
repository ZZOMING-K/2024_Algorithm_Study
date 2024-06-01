import sys

n = int(sys.stdin.readline())
meeting = []

for i in range(n):
    meet = list(map(int, sys.stdin.readline().split()))
    meeting.append(meet)

meeting.sort(key=lambda x: (x[1], x[0]))

current_start, current_end = meeting[0][0], meeting[0][1]   # current_start는 필요 없을듯...
cnt = 1

for i in range(1,n):
    start, end = meeting[i][0], meeting[i][1]

    if start >= current_end:
        cnt += 1
        current_end = meeting[i][1]

print(cnt)