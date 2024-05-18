N = int(input())

stack = []
apndNum = 1
sign = []

prev = 0

make = True

def bigNum(stack, sign, apndNum, target):
    while apndNum <= target:
        stack.append(apndNum)
        apndNum = apndNum + 1
        sign.append('+')
    return stack, sign, apndNum

for i in range(N):
    now = int(input())
    if prev < now:
        stack, sign, apndNum = bigNum(stack, sign, apndNum, now)
        prev = now
        stack.pop()
        sign.append('-')
    else:
        if now == stack.pop():
            prev = now
            sign.append('-')
        else:
            make = False
            break

if make:
    for i in sign:
        print(i)
else:
    print('NO')
