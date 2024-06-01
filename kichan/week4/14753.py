# 14753
import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

cards.sort()

def twoCards(x):
    twoMax1 = x[0] * x[1]
    twoMax2 = x[-1] * x[-2]
    answer1 = max(twoMax1, twoMax2)
    return answer1

def threeCards(x):
    threeMax1 = x[0] * x[1] * x[-1]
    threeMax2 = x[-1] * x[-2] * x[-3]
    answer2 = max(threeMax1, threeMax2)
    return answer2

print(max(twoCards(cards), threeCards(cards)))