n = int(input())
lst1 = [i for i in map(int, input().split())]
m = int(input())
lst2 = [j for j in map(int, input().split())]

lst1.sort()

def bin_search(x, lst, start, end):
    if start > end: # 검색에 실패한 경우
        return False
    
    mid = (start + end) // 2
    if lst[mid] == x: # 검색에 성공한 경우
        return True
    elif x < lst[mid]: # lst의 가운데 값보다 작으면 검색 범위를 처음부터 mid-1까지로 좁힘
        end = mid - 1
        return bin_search(x, lst, start, end)
    else:
        start = mid + 1 # lst의 가운데 값보다 크면 검색 범위를 mid+1부터 끝까지로 좁힘
        return bin_search(x, lst, start, end)

start = 0
end = len(lst1) - 1
for val in lst2: # lst2에 있는 값을 하나씩
    result = bin_search(val, lst1, start, end) # bin_search에 파라미터로 넣어서 확인하고
    if result == True: # 그 결과가 True이면 1 출력
        print(1)
    else:
        print(0) # 아니면 0 출력