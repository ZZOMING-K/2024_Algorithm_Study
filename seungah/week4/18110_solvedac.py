import sys
input = sys.stdin.readline
n = int(input())

def round2(num): 
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if n == 0:
    print(0)
else:
    arr = []
    
    for i in range(n):
        arr.append(int(input()))
        
    arr.sort()
    line = round2(n * 0.15)
    
    if n == 2 * line:
        print(0)
    else:
        finalarr = arr[line:n-line]
        avg = sum(finalarr) / len(finalarr)
        print(round2(avg))

