def solution(n):
    ans = 0 
    while n != 0: # 0번 위치에 도착할 때까지 반복
        if n % 2 == 0: # 2로 나누어지면 항상 순간 이동
            n //= 2
        else: # 2로 나누어지지 않으면 배터리를 1 소모해서 한 칸 이동
            n -= 1
            ans += 1

    return ans