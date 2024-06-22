N = int(input().strip())
primes = [2, 3, 5, 7]

def is_p(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_p(len, num):
    if len == N:
        print(num)
        return
    for d in range(1, 10, 2):
        new_num = num * 10 + d
        if is_p(new_num):
            find_p(len + 1, new_num)

for p in primes:
    find_p(1, p)