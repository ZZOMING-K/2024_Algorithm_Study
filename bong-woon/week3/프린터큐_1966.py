from collections import deque

cases = int(input()) # 테스트 횟수
for _ in range(cases):
    n, m = map(int, input().split()) # n : 문서의 개수, m : 출력 순서가 궁금한 문서의 현재 인덱스
    queue = deque([i for i in map(int, input().split())]) # 중요도랑 상관없이 현재 문서의 배치
    index = deque([i for i in range(len(queue))]) # 현재 배치된 문서의 인덱스
    
    order = 0 # 출력되는 순서를 저장할 변수
    while queue:
        first = queue[0] # 첫번째 문서. popleft()될 때마다 새롭게 갱신

        if first < max(queue):
            queue.append(queue.popleft())
            index.append(index.popleft())
        else:
            queue.popleft()
            check = index.popleft() # popleft() = 프린터 출력
            order += 1 # 출력될 때마다 order + 1
            if check == m:
                print(order)
                break