# 정수 n 입력
n = int(input())

# 원래 자전거 배치 순서 입력
an = list(map(int, input().split()))

# 바뀐 자전거 배치 순서 입력
bn = list(map(int, input().split()))

# 출력값
result = 0 
# an, bn의 원소를 동시에 하나씩 호출하면서 an - bn을 확인
for a, b in zip(an, bn):
    if (a - b) >= 0:
        result += (a - b)

print(result)