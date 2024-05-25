n = int(input())
an = list(map(int, input().split()))
x = int(input())

an.sort()

start = 0
end = len(an) - 1

count = 0
while start < end:
    if an[start] + an[end] == x:
        count += 1
    if an[start] + an[end] < x:
        start += 1
        continue
    end -= 1
    
print(count)