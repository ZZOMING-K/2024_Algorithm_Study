from itertools import permutations

def primenumber(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x >= 3:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

def solution(numbers):
    answer = 0

    prime_lst = []

    for i in range(1, len(numbers) + 1):
        combs = permutations(numbers, i)
        for comb in combs:
            num = ''
            for char in comb:
                num += char

            num = int(num)
            prime_lst.append(num)

    prime_lst = list(set(prime_lst))
    for prime in prime_lst:
        if primenumber(prime) == True:
            answer += 1
    return answer