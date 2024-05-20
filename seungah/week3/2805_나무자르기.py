

N, M = map(int, input().split())  #입력1
trees = list(map(int, input().split()))   #입력2
start, end = 1, max(trees) #범위 설정

while start <= end: #이진탐색
    half = (start+end) // 2
    
    total = 0 
    for i in trees:
        if i >= half:
            total += i - half  # 자를때
    
    if total >= M:
        start = half + 1  #범위 재설정
    else:
        end = half - 1   
print(end)
    
