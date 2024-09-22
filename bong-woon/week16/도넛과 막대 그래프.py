def solution(edges):
    answer = [0, 0, 0, 0]
    edge_dict = {}
    for a, b in edges:
        if not edge_dict.get(a):
            edge_dict[a] = [0, 0]
        if not edge_dict.get(b):
            edge_dict[b] = [0, 0]
        
        edge_dict[a][0] += 1
        edge_dict[b][1] += 1
    
    # print(edge_dict)

    for key, val in edge_dict.items():
        if val[0] >= 2 and val[1] == 0:
            answer[0] = key
        elif val[0] == 0 and val[1] >= 1:
            answer[2] += 1
        elif val[0] >= 2 and val[1] >= 2:
            answer[3] += 1
            
    answer[1] = (edge_dict[answer[0]][0] - answer[2] - answer[3])

    return answer