n = int(input())
seq = [i for i in map(int, input().split())]

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = seq[i] # 첫번째 원소까지 더하는 경우 = 자기 자신
    else:
        dp[i] = max(dp[i - 1] + seq[i], seq[i])

print(max(dp))