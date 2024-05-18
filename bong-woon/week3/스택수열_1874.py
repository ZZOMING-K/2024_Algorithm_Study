n = int(input())

sequence = []
for _ in range(n):
    a = int(input())
    sequence.append(a)

stack = []
outputs = []

i = 0 # sequence의 인덱스
num = 1 # 1부터 n까지 stack에 추가할 원소

while i < n:
    if sequence[i] > num:
        stack.append(num)
        outputs.append('+')
        num += 1
    elif sequence[i] == num:
        stack.append(num)
        outputs.append('+')
        stack.pop()
        outputs.append('-')
        i += 1
        num += 1
    elif sequence[i] < num:
        if stack[-1] == sequence[i]:
            stack.pop()
            outputs.append('-')
            i += 1
        else:
            outputs.append('NO')
            break

if 'NO' not in outputs:
    for output in outputs:
        print(output)
else:
    print('NO')