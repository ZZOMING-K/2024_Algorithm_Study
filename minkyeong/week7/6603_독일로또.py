def recur(start , number) :
    if number == 6 : #재귀함수가 6번 호출 될 경우 배열 print 
        print(*arr)
        return 
    
    for i in range(start,len(nums_list)) :
        arr.append(nums_list[i]) 
        recur(i+1 , number+1) 
        arr.pop() 



while True :
    data = list(map(int,input().strip().split())) #도움받은 코드 
    num = data[0] #집합에 포함되는 숫자의 수 
    nums_list = data[1:] #집합 S에 포함되는 수 
    
    if num == 0 : #0일 나올 경우 while 반복문 중단 
        break 
    
    arr = [] #배열생성 
    recur(0,0) #재귀함수 호출 
    print() #결과들 사이에 한 줄 띄워져야 하므로 print문 추가 