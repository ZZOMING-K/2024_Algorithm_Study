n = int(input())
cards = [i for i in map(int, input().split())]

cards.sort()

result1 = cards[0] * cards[1] # 가장 작은 음수 2개를 곱하는 경우
result2 = cards[-1] * cards[-2] # 가장 큰 양수 2개를 곱하는 경우
result3 = cards[0] * cards[1] * cards[-1] # 가장 작은 음수 2개와 가장 큰 양수 1개를 곱하는 경우
result4 = cards[-1] * cards[-2] * cards[-3] # 가장 큰 양수 3개를 곱하는 경우

print(max(result1, result2, result3, result4))