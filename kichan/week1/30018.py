n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0

for i in range(len(a)):
    if a[i]>b[i]:
        answer += abs(a[i]-b[i])

print(answer)


'''
b의 개수를 a개수에 맞춰야 하기 때문에,
a가 b보다 큰 경우(모자란 경우)만 더해주기
'''
