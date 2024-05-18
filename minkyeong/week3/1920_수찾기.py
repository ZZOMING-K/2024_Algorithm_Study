#오름차순 정렬하여 이분탐색으로 수를 찾았습니다. 
#이분탐색으로 풀지 않을 경우 => 시간초과 발생 

N = int(input())
n_list = list(map(int,input().split()))
M = int(input())
m_list = list(map(int,input().split())) 

n_list.sort() #오름차순 정렬 

start  , end = 0 , len(n_list)-1 

def bisect(arr , target , start , end) : 

    while start <= end :
        mid = (start+end) //2 
        if arr[mid] == target :
            return 1 
        elif arr[mid] > target :
            end = mid -1 
        else :
            start = mid+1 
    return 0 
        
for i in m_list :
    print(bisect(n_list , i , start , end))

#시간초과코드 
# for i in m_list :
#     if i in n_list :
#         print(1)
#     else :
#         print(0)             