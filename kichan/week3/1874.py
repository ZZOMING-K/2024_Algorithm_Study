# 1874

n = int(input())                
stack = []                      # 완성시킬 스택
result = []                     # '+', '-' 를 저장할 리스트 
cnt = 1

for _ in range(n):
    num = int(input())          # 차례로 num을 인풋으로 받음

    while cnt <= num:           # num보다 cnt가 작다면 
        stack.append(cnt)       # 스택에 추가
        result.append('+')      # 추가 -> '+'
        cnt += 1                # num보다 커지면 멈춤
    
    if stack[-1] == num:        # 스택의 마지막 숫자를
        stack.pop()             # 꺼내주기
        result.append('-')      # 꺼냄 -> '-'
    
if len(stack) == 0:             # 정상작동했다면 스택은 비게 됨
    for i in result:
        print(i)
else:
    print('NO')

'''
    1~n의 숫자를 인풋으로 들어오는 값에 맞춰줘야 함
    
    (Ex.) 
    n=8이라면, [1,2,3...8]을
    [4,3,6,8,7,5,2,1] 에 맞춰줘야 하기 때문에 
    
    첫번째 num은 4,
    - 4이하의 숫자들(1,2,3,4)이 차례로 스택에 들어감 => cnt: 4
    - 스택의 마지막 숫자가 num과 같기 때문에 pop

    두번째 num은 3, cnt가 더 크므로 스택에 추가되지 않음
    - 스택의 마지막 숫자가 num과 같기 때문에 pop

    반복...

    만약, 정상적으로 끝까지 진행되었다면, stack은 빌 것이기 때문에,
    stack이 비어 있다면 result의 +,-를 출력해주고
    아니라면, 'NO' 출력
'''