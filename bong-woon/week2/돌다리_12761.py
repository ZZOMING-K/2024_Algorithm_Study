from collections import deque

a, b, n, m = map(int, input().split())
check = [False] * 10000
moves = ['+1', '-1', '+' + str(a), '-' + str(a), '+' + str(b), '-' + str(b), '*' + str(a), '*' + str(b)]


def bfs(x, y):
    count = 0
    check[x] = True
    x_str = str(x)
    q = deque()
    q.append(x_str)

    while q:
        cur_loc = q.popleft()

        for i in range(8):
            nex_loc = cur_loc + moves[i]
            print(nex_loc)
            nex_loc_val = eval(nex_loc)
            print(nex_loc_val)
            if nex_loc_val < 0 or nex_loc_val > 100000:
                continue
            elif 0 <= nex_loc_val <= 100000 and check[nex_loc_val] == False:
                check[nex_loc_val] = True
                q.append(str(nex_loc_val))
                count += 1
                if nex_loc_val == y:
                    return print(count)
        
bfs(n, m)