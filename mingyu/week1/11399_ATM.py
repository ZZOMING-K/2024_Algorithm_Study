N = input()
A = list(map(int, input().split()))

A.sort()

answer = 0
waitTime = 0
for i in A:
    answer = answer + i + waitTime
    waitTime = waitTime + i

print(answer)
