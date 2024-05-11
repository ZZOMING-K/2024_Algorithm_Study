import math

a = list(input())
start_set = []
sum = 0

for i in range(len(a)-1):
    if a[i] == a[i+1]:
        pass
    else:
        sum += 1
sum = (math.ceil(sum/2))

print(sum)