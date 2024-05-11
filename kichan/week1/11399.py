n = int(input())
people = list(map(int, input().split()))

result = 0
answer = 0

people.sort()

for i in range(n):
    result += people[i]
    answer += result

print(answer)

'''
n      : 사람수
people : 각 사람들의 걸리는 시간

result에는 누적된 시간들을 더해주고
answer에 그 값들을 더해주기
'''