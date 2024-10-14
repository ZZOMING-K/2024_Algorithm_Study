def solution(a):
    n = len(a)
    if n <= 2:
        return n

    left_min = [0] * n # 자기 자신을 포함한 왼쪽에 위치한 값들 중에서 최솟값
    right_min = [0] * n # 자기 자신을 포함한 오른쪽에 위치한 값들 중에서 최솟값
    
    left_min[0] = a[0] # 리스트의 첫번째 원소는 왼쪽에 더 원소가 없으므로 자기 자신이 최솟값
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])
    
    right_min[n - 1] = a[n - 1] # 리스트의 마지막 원소는 오른쪽에 더 원소가 없으므로 자기 자신이 최솟값
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])
    
    answer = 2
    for i in range(1, n - 1):
        if a[i] > left_min[i - 1] and a[i] > right_min[i + 1]: # 값이 작은 풍선을 터트리는 행동을 한 번 밖에 할 수 없기 때문에 a[i]는 마지막까지 남겨둘 수 없음
            continue
        answer += 1
    
    return answer
