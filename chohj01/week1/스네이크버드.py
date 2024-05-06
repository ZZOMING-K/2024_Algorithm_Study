import sys
nn= list(map(int,input().split()))
n=nn[0]
l=nn[1]


f = list(map(int, input().split()))
s = []

s = sorted(f)
for i in range(n):
    if l >= s[i]:
        l = l + 1
    else:
        print(l)
        sys.exit()
print(l)