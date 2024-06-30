n = int(input())

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

def backtrack(x, lst, count, n):
    if count == n:
        lst.append(x)
        return
    
    for i in range(1, 10, 2):
        if primenumber(x * 10 + i) == True:
            backtrack(x * 10 + i, lst, count + 1, n)

lst = []
count = 1
prime_numbers = [2, 3, 5, 7]

if n == 1:
    for num in prime_numbers:
        print(num)
elif n >= 2:
    for num in prime_numbers:
        backtrack(num, lst, count, n)
    
    for ans in lst:
        print(ans)