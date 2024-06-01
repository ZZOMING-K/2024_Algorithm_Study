n = int(input())

table = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n
color_lst = []

for i in range(n):
    if i == 0:
        dp[i] = min(table[i])
        color_idx = table[i].index(min(table[i]))
    else:
        for j, color in enumerate(table[i]):
            if color_idx == j:
                continue
            else:
                color_lst.append((j, color))
        
        color_lst.sort(key = lambda x : x[1])
        dp[i] = dp[i - 1] + color_lst[0][1]
        color_idx = color_lst[0][0]
        color_lst.clear()

print(dp[-1])