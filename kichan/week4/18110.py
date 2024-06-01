
import sys

n = int(sys.stdin.readline().rstrip())

def roundup(num):
    if num - int(num) >= 0.5:
        num = int(num) + 1
    else:
        num = int(num)

    return num

if n == 0:
    print(0)
else:
    score = []
    for _ in range(n):
        score.append(int(sys.stdin.readline().rstrip()))

    score.sort()
    sc = roundup(n*0.15)

    print(roundup(sum(score[sc:n-sc])/len(score[sc:n-sc])))