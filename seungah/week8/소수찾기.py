def solution(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    answer = 0
    all_comb = set()

    # 가능한 모든 숫자 조합을 생성
    def combinations(remain, current):
        nonlocal answer
        if current != "":
            num = int(current)
            if num not in all_comb:
                all_comb.add(num)
                if is_prime(num):
                    answer += 1
        for i in range(len(remain)):
            combinations(remain[:i] + remain[i+1:], current + remain[i])

    combinations(numbers, "")

    return answer

