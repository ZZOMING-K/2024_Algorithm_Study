n = int(input())
lst = [i for i in map(int, input().split())]

lst.sort()

start = 0
end = len(lst) - 1

if lst[start] > 0 and lst[end] > 0:
    print(lst[start], lst[start+1])

elif lst[start] < 0 and lst[end] < 0:
    print(lst[end-1], lst[end])

elif lst[start] * lst[end] < 0:
    while start <= end:
        mid = (start + end) // 2
        mixed = lst[start] + lst[mid]

        if mixed < lst[mid]:
            start = mid + 1
        elif mixed > lst[mid]:
            end = mid - 1

    print(lst[start], lst[end])