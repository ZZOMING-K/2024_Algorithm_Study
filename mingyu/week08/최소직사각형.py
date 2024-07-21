def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
    sizes.sort()
    walletx = sizes[-1][0]
    wallety = sizes[-1][1]
    if walletx == wallety:
        return walletx ** 2
    else:
        return walletx * sorted(sizes, key = lambda x : x[1])[-1][1]
