N = int(input())
test = [int(input()) for _ in range(N)]
result = [1, 1, 1]
for i in range(3, max(test)+1):
    result.append(result[i-2] + result[i-3])
for i in test:
    print(result[i-1])
