N = int(input())
romanNum = [1, 5, 10, 50]
tmp = []
check = {}
for i in range(1, N + 1):
    check[i] = []

def func(now, step):
    if step == N + 1:
        tmp.append(now)
    else:
        
        for i in range(4):
            if not now+romanNum[i] in check.get(step, []):
                func(now + romanNum[i], step + 1)
                check[step].append(now + romanNum[i])
            

func(0, 1)
#print(tmp)
#print(check)
print(len(tmp))
