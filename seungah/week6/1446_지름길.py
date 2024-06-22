N, D = map(int, input().split())
route = []
da = [i for i in range(D + 1)]

for _ in range(N):
    start, end, time = map(int, input().split())
    if end <= D:
        route.append((start, end, time))


route.sort()


for i in range(D + 1):
    if i != 0:
        da[i] = min(da[i], da[i - 1] + 1)
    for start, end, time in route:
        if start == i and end <= D and da[end] > da[start] + time:
            da[end] = da[start] + time

print(da[D])