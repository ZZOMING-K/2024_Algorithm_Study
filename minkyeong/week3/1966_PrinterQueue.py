#1. 문서의 중요도가 큰 수 부터 출력해줘야 하기에, 만일 중요도가 낮을 경우에는 뒤에 append 처리 
#2. 중요도가 같을 경우도 있기 때문에 value 가 아닌 index를 기준으로 몇번째로 출력하는지 count 를 세주었습니다.  


from collections import deque

def find_count() : 
    N , M = map(int,input().split()) #문서의 개수, 몇번째로 인쇄되었는지 궁금한 문서 위치 입력 
    num_list = deque(list(map(int,input().split()))) #문서의 중요도 입력 


    new_q = deque()
    for idx,num in enumerate(num_list) : #문서의 중요도가 같을 경우를 구분하기 위해 index 와 함께 큐 생성 
        new_q.append((idx , num)) 

    count = 0     

    while len(new_q) > 0 : #큐가 빌 때 까지 반복 
    
        max_num = max(new_q , key = lambda x : x[1])[1] #value값을 기준으로 최대 값 도출 
        
        x = new_q.popleft()  #( key, value ) 쌍을 꺼내어 만일 중요도가 가장 큰 경우가 아닐 경우 젤 뒤에 append 
    
        if x[1] == max_num : # 만일 최댓값 (높은 중요도) 일 경우 popleft 후, count 세기 
            count+=1
        
            if x[0] == M : # 몇번 째로 인쇄되는지 알고자하는 문서였을 경우 count 출력하고 반복문 멈추기 
                return count 
                break
        
            continue
    
        new_q.append(x) 

T = int(input())  # 몇번 테스트할 건지 입력  
for _ in range(T):
    answer = find_count() #find_count 함수 실행 
    print(answer)
    