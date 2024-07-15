N = input()

isMultipleOfTen = False
sumOfDigit = 0

sortN = []
for i in N:
    i = int(i)
    if i == 0:
        isMultipleOfTen = True
    sumOfDigit = sumOfDigit + i
    sortN.append(int(i))

if not isMultipleOfTen or sumOfDigit % 3 != 0:
    print(-1)
else:
    for i in sorted(sortN, reverse = True):
        print(i, end= '')
