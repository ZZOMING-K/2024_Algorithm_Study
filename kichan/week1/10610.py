n = str(input())

result = 0
answer = -1

if '0' not in n:
    print(answer)

else:
    for i in range(len(n)):
        result += int(n[i])
    
    if result%3 != 0:
        print(answer)
    else:
        answer = sorted(n,reverse=True)
        print(''.join(answer))

'''
    30의 배수인지 체크
    1. 10의 배수인지 -> 0이 포함되어야 한다
    2. 3의 배수인지 -> 모든 자리 수의 합이 3의 배수이어야 함

    result : 모든 자리 수의 합

    가장 큰 수를 찾는 것이기 때문에, 내림차순 정렬해서 이어주면 됨
'''