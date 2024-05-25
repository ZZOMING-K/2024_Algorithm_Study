n = int(input())

lst = []

for _ in range(n):
    lst.append(int(input()))

def round_up(x):
    if x - int(x) >= 0.5:
        return int(x+1)
    else:
        return int(x)

lst.sort()
trim = round_up(len(lst) * 0.15)
trim_lst = lst[trim:len(lst) - trim]

tier = 0
try:
    tier = round_up(sum(lst[trim:len(lst) - trim]) / len(lst[trim:len(lst) - trim]))
except ZeroDivisionError:
    pass
print(tier)