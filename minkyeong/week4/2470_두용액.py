
n = int(input())
n_list = list(map(int, input().split()))

current = float('inf')
answer = None


for i in range(len(n_list) - 1):
    for j in range(i + 1, len(n_list)):
        
        abs_sum = abs(n_list[i] + n_list[j])

        if abs_sum < current:
            current = abs_sum
            answer = (n_list[i], n_list[j])

print(answer[0], answer[1])