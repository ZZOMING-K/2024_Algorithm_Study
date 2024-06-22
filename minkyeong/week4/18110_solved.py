#round함수 사용 ⇒ runtime error 발생 

from sys import stdin


def rdup(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(stdin.readline())

if n == 0:
    print(0)

else : 
    
    level_list = sorted([int(stdin.readline()) for _ in range(n)])
    except_num = rdup(n * 0.15)
    
    print(rdup(sum(level_list[except_num:n-except_num])/len(level_list[except_num:n-except_num])))