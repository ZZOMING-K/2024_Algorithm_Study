import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
max_res = -float('inf')
min_res = float('inf')

def dfs(idx, curr_res, add, sub, mul, div):
    global max_res, min_res
    if idx == N:
        max_res = max(max_res, curr_res)
        min_res = min(min_res, curr_res)
        return
    if add > 0:
        dfs(idx + 1, curr_res + nums[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, curr_res - nums[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, curr_res * nums[idx], add, sub, mul - 1, div)
    if div > 0:
        dfs(idx + 1, int(curr_res / nums[idx]), add, sub, mul, div - 1)

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(max_res)
print(min_res)