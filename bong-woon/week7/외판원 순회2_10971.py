n = int(input())

info = [list(map(int, input().split())) for _ in range(n)]
lst = []

def travel(x, start, check, lst, dist, count):
    if sum(check) == n and info[x][start] != 0:
        lst.append(dist + info[x][start])
        return lst
    
    check[x] = True
    for i in range(n):
        if check[i] == False and info[x][i] != 0:
            check[i] = True
            travel(i, start, check, lst, dist + info[x][i], count + 1)
            check[i] = False

for num in range(n):
    check = [False] * n
    dist = 0
    count = 0
    travel(num, num, check, lst, dist, count)

print(min(lst))