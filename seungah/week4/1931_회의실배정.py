# 실행은 맞게 되는데 틀리게 나옵니다
N = int(input())

meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: x[1])

end_time = 0
count = 0
for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)