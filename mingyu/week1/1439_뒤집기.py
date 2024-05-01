A = input()
standard = A[0]
isContinue = False

answer = 0

for i in A:
    if i != standard and not isContinue:
        isContinue = True
        answer = answer + 1
    elif i != standard and isContinue:
        continue
    else:
        isContinue = False

print(answer)
