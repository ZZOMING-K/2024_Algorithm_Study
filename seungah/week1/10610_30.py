'''
Q:10610
1. 숫자 입력
2. 숫자마다 분할 후 리스트 N으로 적재
3. 나열 후 30의 배수인지 확인
    1. 0이 들어가는지 확인
    2. 모든 수의 합이 3으로 나눠지는지 확인
    3. 내림차순 정렬 
    4. 리스트 붙인 후 출력
'''


inp = input()  #1
N = [int(char) for char in inp]  #2
if 0 not in N:  #3-1
    print(-1)
else:
    sum = 0
    for i in N:
        sum += i
    if sum % 3 != 0:  #3-2
        print(-1)
    else:
        N = sorted(N, reverse=True)  #3-3
        N = [str(int) for int in N]
        print(''.join(N))

