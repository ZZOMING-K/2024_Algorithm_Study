'''N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i - 1, 0, -1):
        if arr[j] < arr[i]:
            dp[i] = dp[j] + 1
            break

print(max(dp))'''

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i - 1, -1, -1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))