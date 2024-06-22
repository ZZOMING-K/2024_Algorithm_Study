
N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))
#print(stairs)

dp = [[0, 0] for i in range(N)]
dp[-1] = [stairs[-1], 0]

answer = 0

for i in range(len(stairs) - 1, -1, -1):        #계단 내려옴
    for j, value in enumerate(dp[i]):
        if value == 0:
            continue
        if j == 1:      # 두 칸 내려와야 하는 경우
            if i - 2 >= 0:
                if dp[i - 2][0] <= value + stairs[i - 2]:
                    dp[i - 2][0] = value + stairs[i - 2]
        else:
            if i - 2 >= 0:
                if dp[i - 2][0] <= value + stairs[i - 2]:
                    dp[i - 2][0] = value + stairs[i - 2]
            if i - 1 >= 0:
                if dp[i - 1][1] <= value + stairs[i - 1]:
                    dp[i - 1][1] = value + stairs[i - 1]
'''
for i in dp:
    print(i)
        
'''
if N == 1:
    print(dp[0][0])
else:
    print(max(dp[0][0], dp[0][1], dp[1][1]))
