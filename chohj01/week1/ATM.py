n = int(input())
a = list(map(int, input().split()))
s = 0

a = sorted(a)
b = []

for i in a:
    s += i
    b.append(s)
print(sum(b))