test = int(input())

for _ in range(test):
    pn = int(input())
    dp = [1] * pn

    idx = 0
    for i in range(pn):
        if i <= 2:
            dp[i] = 1 # 처음 3개의 정삼각형의 변의 길이 = 1
        elif i <= 4:
            dp[i] = 2 # 그 다음 2개의 정삼각형의 변의 길이 = 2
        elif i >= 5:
            dp[i] = dp[i - 1] + dp[idx]
            idx += 1
    
    print(dp[pn - 1])