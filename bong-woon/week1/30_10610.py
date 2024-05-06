# 양수 n 입력
n = input()

# 양수 n을 구성하는 숫자를 저장할 리스트
lst = []

# 양수 n의 모든 자릿수의 합
sum = 0

# 입력한 양수를 구성하는 숫자들을 하나씩 lst에 추가하고
# 정수형으로 바꿔주고 자릿수의 합을 sum에 저장
for num in n:
    lst.append(num)
    sum += int(num)

# sum이 3의 배수가 아니면 30의 배수가 아니므로 -1
if sum % 3 != 0:
    print(-1)
else: # sum이 3의 배수이더라도 일의 자리가 0이 아니면 30의 배수가 아니므로 -1
    lst.sort(reverse = True) # 내림차순으로 정렬했을 때 마지막 원소(일의 자리가) 0인지 확인 & 최댓값을 구하기 위해 각각의 자릿수를 내림차순으로 정렬
    if lst[-1] != '0':
        print(-1)
    else:
        # 30의 배수 중 최댓값을 저장할 빈 문자열
        max_num = ''

        # lst의 원소를 앞에서부터 하나씩 이어붙인다
        # 내림차순 정렬을 했기 때문에 이어붙인 값이 최댓값이 된다.
        for num in lst:
            max_num += num

        print(int(max_num))