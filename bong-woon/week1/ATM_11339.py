# 줄을 선 사람의 수
n = int(input())

# 앞에 선 사람부터 소요 시간을 입력
pi = list(map(int, input().split()))
# 오름차순 정렬
pi.sort()

# 최소 소요 시간을 저장하기 위한 초기화
result = 0
# pi의 값과 인덱스 정보를 모두 차례대로 확인
for i, val in enumerate(pi):
    # 제일 앞에 선 사람은 i = 0이고 n번만큼 더해지므로 val * (len(pi) - i)
    result += val * (len(pi) - i)

print(result)