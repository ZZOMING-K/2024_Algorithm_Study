number = list(map( int, input()))
number.sort(reverse = True)

if sum(number)%3 == 0 and number[-1] == 0:
    a = ("".join(map(str, number)))
    print(a)
else:
    print("-1")