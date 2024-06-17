#실패
V, E = map(int, input().split())
K = int(input())
graph = []

for i in range(E):
    v1, v2, w = map(int, input().split())