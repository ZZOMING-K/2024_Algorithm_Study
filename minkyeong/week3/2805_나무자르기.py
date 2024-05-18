#1. 만일 나무의 길이가 절단점보다 클 경우 total(가져갈 수 있는 나무의 길이)에 누적계산 
#2. 이때 total은 적어도 M보다 커야 한다. (M보다 작을 경우 끝점을 mid-1로 설정, M보다 클경우 시작점을 절단점+1로 설정) 
#3. 가장 큰 나무를 기준으로 이분탐색을 실시하여 적절한 절단점 계산  

N , M = map(int,input().split()) 
tree_list = list(map(int,input().split())) 

start , end = 0 , max(tree_list)
result = 0 

while start <= end :
    mid = (start + end) // 2 #절단점 
    total = 0 #가져갈 수 있는 나무의 길이 
    
    for tree in tree_list : 
        if tree > mid : #만일 나무의 길이가 절단점 보다 크다면, total에 누적
            total += tree - mid 
            
    if total < M : #만일 나무의 길이가 M보다 작을 경우 끝점을 mid-1 로 설정 (절단점을 작게 설정 하기 위해)
        end = mid - 1 
    else :
        result = mid #만일 나무의 길이가 M보다 클 경우 끝점을 mid+1로 설정(절단점을 크게 설정 하기 위해)
        start = mid+1 
        
print(result)
          
        
