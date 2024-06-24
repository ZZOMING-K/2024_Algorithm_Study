def recur(cur, start):

    if cur == 6:
        print(' '.join(map(str,answer)))
        return
    
    for i in range(start,k):
        answer.append(numbers[i])
        recur(cur+1,i+1)
        answer.pop()

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    numbers = arr[1:]
    answer = []
    recur(0,0)

    if k == 0:
        exit()
    print()