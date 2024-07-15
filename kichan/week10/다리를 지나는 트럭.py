from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    n = bridge_length
    trucks = deque(truck_weights)
    bridge = deque([0 for _ in range(n)])
    current_weight = 0
    
    while trucks:
        answer += 1
        current_weight -= bridge.popleft()
        
        if current_weight + trucks[0] <= weight:
            current_weight += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
        
    answer += n
    
    return answer