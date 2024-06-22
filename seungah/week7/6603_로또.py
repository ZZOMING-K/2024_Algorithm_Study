import sys
input = sys.stdin.readline

def backtrack(start, nums):
    if len(nums) == 6:
        print(' '.join(map(str, nums)))
        return
    for i in range(start, k):
        backtrack(i + 1, nums + [S[i]])

while True:
    line = input().strip()
    if line == "0":
        break
    data = list(map(int, line.split()))
    k = data[0]
    S = data[1:]
    
    backtrack(0, [])
    print()