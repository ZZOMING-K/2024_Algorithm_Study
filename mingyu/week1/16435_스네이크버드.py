N, L = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

for i in H:
    if L >= i:
        L = L + 1
    else:
        break
print(L)
