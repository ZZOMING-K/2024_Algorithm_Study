import sys

N = int(input())
graph = [ list(input().split()) for _ in range(N) ]  

#sys 모듈 사용하여 시스템이 가장 높은 값과 가장 낮은 값을 지정 
max_answer = -sys.maxsize
min_answer = sys.maxsize

# 아래, 오른쪽만 이동 가능 
dy = [1,0]
dx = [0,1]


def dfs(y,x, curr_num, operate):  # 좌표 , 누적연산값 
    global max_answer, min_answer

    if y == N - 1 and x == N - 1:  #만일 학교에 도착했을 경우 정답 업데이트 
        max_answer = max(max_answer, int(curr_num))
        min_answer = min(min_answer, int(curr_num))

    # 아래, 오른쪽만 이동 
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        # 만일 범위를 벗어나면 무시하기 
        if nx >= N or ny >= N:
            continue

        if graph[ny][nx].isdigit():  # 만일 숫자라면 eval 함수를 사용해 누적된 숫자와 현재 숫자와 연산  
            dfs(ny, nx, str(eval(curr_num + operate + graph[ny][nx])), '')
        else:  
            dfs(ny, nx, curr_num, graph[ny][nx])


dfs(0, 0, graph[0][0], '') #0,0 위치에서 출발하며 현재 연산할 숫자는 0,0에 위치한 숫자  
print(max_answer, min_answer)