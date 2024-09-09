def solution(n, costs):
    answer = 0
    connects = [[]]
    loc = []
    for i, cost in enumerate(costs):
        loc.append([cost[2], i])
    loc.sort(reverse = True)
    while len(connects[0]) != n:
        now = loc.pop()
        nowloc = now[1]
        x = costs[nowloc][0]
        y = costs[nowloc][1]
        nowcost = now[0]
        merged = False
        for i, connect in enumerate(connects):
            if merged:
                break
            if x in connect or y in connect:
                if x in connect and y in connect:
                    merged = True
                    break
                for j in range(i + 1, len(connects)):
                    if merged:
                        break
                    if x in connects[j] or y in connects[j]:
                        connects[i].append(x)
                        connects[i].append(y)
                        answer = answer + nowcost
                        while connects[j]:
                            now = connects[j].pop()
                            connects[i].append(now)
                        merged = True
                        connects[i] = list(set(connects[i]))
                        break
                if not merged:
                    connects[i].append(x)
                    connects[i].append(y)
                    merged = True
                    connects[i] = list(set(connects[i]))
                    answer = answer + nowcost
                    break
        if not merged:
            if not connects[0]:
                connects[0].append(x)
                connects[0].append(y)
            else:
                connects.append([])
                connects[-1].append(x)
                connects[-1].append(y)
            answer = answer + nowcost
    return answer
