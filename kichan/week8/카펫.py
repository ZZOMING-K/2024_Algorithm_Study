def solution(brown, yellow):

    square = brown+yellow
    
    for height in range(3,int(square**0.5)+1):
        if square%height==0:
            width = square//height
            
            if (width-2)*(height-2) == yellow:
                return [width,height]