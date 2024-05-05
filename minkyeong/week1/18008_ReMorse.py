from collections import Counter

s = input()
filter_s ="".join([char.upper() for char in s if char.isalpha()]) 

answer = sorted(list(Counter(filter_s).values()), reverse=True)


current_number = 1 
fib1, fib2 = 1, 2  
result = []

n = len(answer)

while len(result) < n:
     
    result.extend([current_number] * fib1) 
    current_number += 2
    fib1, fib2 = fib2, fib1 + fib2 


result = sum([a*b for a, b in zip(answer, result)]) + (len(filter_s) - 1) * 3
print(result)