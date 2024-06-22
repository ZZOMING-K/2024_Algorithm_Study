from itertools import combinations_with_replacement

n = int(input())
roma = [1, 5, 10, 50]

combs = combinations_with_replacement(roma, n)

lst = []
for comb in combs:
    lst.append(sum(comb))

print(len(set(lst)))