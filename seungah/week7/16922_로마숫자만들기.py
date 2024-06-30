
import sys
input = sys.stdin.readline

N = int(input())
roman = [1, 5, 10, 50]
romanswer = set()

def recur(num, sum):
    if num == N:
        romanswer.add(sum)
        return
    for i in roman:
        recur(num + 1, sum + i)

recur(0, 0)
print(len(romanswer))