n = int(input())

numbers = [1,5,10,50]
arr = [0]*1001
num = 0

def recur(cur, start):

    if cur == n:
        global num
        arr[num] = 1
        return
    
    for i in range(start,4):
        num += numbers[i]
        recur(cur+1,i)
        num -= numbers[i]

recur(0,0)
print(sum(arr))