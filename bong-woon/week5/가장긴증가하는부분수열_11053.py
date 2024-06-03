n = int(input())

seq = [i for i in map(int, input().split())]
dp = [1] * n

for i in range(1, n):
    for j in range(0, i): # seq[i]보다 앞에 있는 원소들을 확인
        if seq[j] < seq[i]: # seq[i]보다 앞에 있는 원소들 중에 seq[i]보다 작으면
            dp[i] = max(dp[i], dp[j] + 1) # dp[i]를 갱신

print(max(dp))