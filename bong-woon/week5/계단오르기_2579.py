n = int(input())

scores = []
for _ in range(n):
    scores.append(int(input()))
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = scores[i] # 첫번째 계단까지 오를 때 최댓값
    elif i == 1:
        dp[i] = scores[i - 1] + scores[i] # 두번째 계단까지 오를 때까지 최댓값
    else:
        dp[i] = max(dp[i - 3] + scores[i - 1] + scores[i], dp[i - 2] + scores[i])

print(dp[n - 1])