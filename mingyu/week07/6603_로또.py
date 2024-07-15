#import time

def lotto(k, step):
    if step == 7:
        for i in tmp:
            print(i, end = ' ')
        print()
        return
    
    else:
        for i in range(0, len(k)):
            if 6 - step < len(k) - i :
                tmp.append(k[i])
                lotto(k[i+1:], step + 1)
                tmp.pop()
                #time.sleep(0.1)

firstTime = True

while True:
    k = list(map(int, input().split()))
    if k == [0]:
        break
    
    if firstTime:
        firstTime = False
    else:
        print()

    chk = [False for i in range(len(k) + 1)]
    tmp = []
    lotto(k[1:], 1)
