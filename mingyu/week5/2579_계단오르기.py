###각 계단마다 몇 번의 연속된 step으로, 최대값을 낼 수 있는지를 저장해야 할듯?
#연속된 세 개의 계단을 밟으면 안됨
#몇 번 연속으로 밟았는지와 그때의 최대값을 같이 저장해야 함
#마지막 계단은 반드시 밟아야 함 -> 문제 풀이의 힌트가 될 수도 있을듯?
#마지막부터 내려오는 방식으로 접근해보자!

#True, 1, 20 -> False, 2, 30 / True 3, 45 ->
#False면 1을 못 더함
#True면 1을 더해 False가 될 수도, 2를 더해 True가 될 수도 있음
#[2]가 N+1이 되면 종료

#첫 번째 계단 반드시 밟아야 함
#두 번째 계단부터 True인 경우, False인 경우 나눠서 배열에 저장해야 함
#dp[0]에 True인경우, [1]에 False인 경우 저장하자
#못 가는 경우는 0

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
