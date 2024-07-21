N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

answer = []

def calc(A, add, sub, mul, div, res):
    if not(A):
        answer.append(res)
    else:
        if add > 0:
            calc(A[1:], add-1, sub, mul, div, res + A[0])
        if sub > 0:
            calc(A[1:], add, sub-1, mul, div, res - A[0])
        if mul > 0:
            calc(A[1:], add, sub, mul-1, div, res * A[0])
        if div > 0:
            if res < 0:
                res = res * -1
                calc(A[1:], add, sub, mul, div-1, res // A[0] * -1)
            else:
                calc(A[1:], add, sub, mul, div-1, res // A[0])
calc(A[1:], add, sub, mul, div, A[0])
print(max(answer))
print(min(answer))
