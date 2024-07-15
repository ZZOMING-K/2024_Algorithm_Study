n = int(input())
A = list(map(int, input().split()))
x = int(input())

A.sort()

answer = 0

for i, j in enumerate(A):
    target = x - j
    if i != len(A) - 1:
        start = i + 1
        end = len(A) - 1
        mid = (start + end) // 2

        while start <= end:
            if A[mid] == target:
                answer = answer + 1
                break
            
            elif A[mid] < target:
                start = mid + 1
                mid = (start + end) // 2

            else:
                end = mid - 1
                mid = (start + end) // 2

print(answer)
