n = int(input())
info = [list(input().split()) for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

lst = [] # 완성된 식을 저장할 리스트
text = '' # 숫자와 연산자를 하나씩 더해가면서 식을 완성할 문자열
def dfs(x, y, info, text):
    if x == n-1 and y == n-1:
        text += info[x][y]
        lst.append(text)
        return lst
    else:
        text += info[x][y]

        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx > n-1 or ny > n-1:
                continue
            else:
                dfs(nx, ny, info, text)
    return lst
    
all_cases = dfs(0, 0, info, text)


######### 계산
results = []

for eq in all_cases:
    cal_result = 0
    current_str = ''

    for i, s in enumerate(eq):
        current_str += s
        if i != 0 and i % 2 == 0:
            cal_result = eval(current_str)
            current_str = str(cal_result)
    results.append(cal_result)

print(max(results), min(results))