def solution(bridge_length, weight, truck_weights):
    answer = 0
    onbridge = [[0, 1]]
    onbridgeweight = 0
    
    while onbridge:
        answer = answer + 1
        
                
        for i in range(len(onbridge)):
            onbridge[i][1] = onbridge[i][1] - 1

        if onbridge[0][1] == 0:
                onbridgeweight = onbridgeweight - onbridge[0][0]
                onbridge = onbridge[1:]
        
        if truck_weights and weight >= truck_weights[0] + onbridgeweight:
            onbridge.append([truck_weights[0], bridge_length])
            onbridgeweight = onbridgeweight + truck_weights[0]
            truck_weights = truck_weights[1:]

        
        #print(answer)
        #print(onbridge)
    return answer