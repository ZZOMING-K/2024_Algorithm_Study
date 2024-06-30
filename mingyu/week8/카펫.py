def solution(brown, yellow):
    for w in range(1, 2000001):
        for h in range(1, 2000001):
            if h > w:
                break
            if w * h == yellow:
                if (w + 2) * (h + 2) - yellow == brown:
                    return [w + 2, h + 2]
