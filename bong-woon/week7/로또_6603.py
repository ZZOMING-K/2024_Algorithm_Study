from itertools import combinations

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    else:
        lst = lst[1:]

    combs = combinations(lst, 6)
    for comb in combs:
        for num in comb:
            print(num, end = ' ')
        print(' ')
    print(' ')