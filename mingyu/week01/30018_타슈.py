n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0

for i in range(n):
    if B[i] > A[i]:
        answer = answer + B[i] - A[i]
print(answer)
