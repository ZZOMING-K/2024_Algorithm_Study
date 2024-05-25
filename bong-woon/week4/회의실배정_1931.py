n = int(input())

times = []
for _ in range(n):
    times.append(list(map(int, input().split())))
sorted_times = sorted(times, key = lambda x : (x[1], x[0]))

idx = 0
count = 1

for i in range(1, n):
    if sorted_times[idx][1] <= sorted_times[i][0]:
        count += 1
        idx = i

print(count)