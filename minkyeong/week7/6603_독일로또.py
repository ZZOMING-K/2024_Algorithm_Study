def recur(number ,start) :
    if number == 6 : #만일 숫자가 6개라면 출력 
        print(*arr)
        return 
    
    for i in range(start , len(nums_list)) : 
        arr.append(nums_list[i])
        recur(number+1 , i +1)
        arr.pop() 



while True :
    data = list(map(int,input().strip().split())) #도움받은 코드 
    num = data[0]
    nums_list = data[1:]
    
    if num == 0 : #0일 나올 경우 while 반복문 중단 
        break 
    
    arr = []
    recur(0,0) 
    print() #결과들 사이에 한 줄 띄워쟈 하므로 print문 추가 