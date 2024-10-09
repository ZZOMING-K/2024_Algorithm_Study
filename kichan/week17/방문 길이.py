def solution(dirs):
    
    path = set()
    x,y=0,0
    
    for d in dirs:
        if d == 'U':
            if y+1 <= 5:
                new_y = y+1
                path.add(((x,y),(x,new_y)))
                path.add(((x,new_y),(x,y)))
                y = new_y
                
        elif d == 'D':
            if y-1 >= -5:
                new_y = y-1
                path.add(((x,y),(x,new_y)))
                path.add(((x,new_y),(x,y)))
                y = new_y
                
        elif d == 'R':
            if x+1 <= 5:
                new_x = x+1
                path.add(((x,y),(new_x,y)))
                path.add(((new_x,y),(x,y)))
                x = new_x
                
        elif d == 'L':
            if x-1 >= -5:
                new_x = x-1
                path.add(((x,y),(new_x,y)))
                path.add(((new_x,y),(x,y)))
                x = new_x
                
    answer = len(path)//2
                
    return answer