def solution(numbers, target):
    answer = 0

    def dfs(start, total):
        nonlocal answer
        if start == len(numbers):
            if total == target:
                answer += 1
            return

        dfs(start + 1, total + numbers[start])
        dfs(start + 1, total - numbers[start])
    
    dfs(0, 0)
    
    return answer