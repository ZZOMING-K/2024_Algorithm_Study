def solution(maps):
    def isvalid(x, y):
        if x >= 0 and x < len(maps[0]) and y >= 0 and y < len(maps):
            return True
        else:
            return False
    
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    
    maps[0][0] = 0
    nowbfs = [[0, 0]]
    nextbfs = []
    level = 0
    
    while True:
        if not nowbfs:
            return -1
        level = level + 1
        while nowbfs:
            now = nowbfs.pop()
            
            if now[0] == len(maps) - 1 and now[1] == len(maps[0]) - 1:
                return level
            
            for i in range(4):
                y = now[0] + move[i][0]
                x = now[1] + move[i][1]
                if isvalid(x, y) and maps[y][x] == 1:
                    #print(y, x)
                    maps[y][x] = 0
                    nextbfs.append([y, x])
        nowbfs = nextbfs
        nextbfs = []
