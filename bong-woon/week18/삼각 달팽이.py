def solution(n):
    triangle = [[0] * i for i in range(1, n+1)]
    
    x, y = -1, 0  # 초기 시작은 (0,0)이 될 것임
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1  # 아래로 이동
            elif i % 3 == 1:
                y += 1  # 오른쪽으로 이동
            else:
                x -= 1
                y -= 1  # 대각선 왼쪽 위로 이동
            triangle[x][y] = num
            num += 1

    answer = []
    for row in triangle:
        answer += row
    
    return answer