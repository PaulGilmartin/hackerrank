from collections import deque
N = int(input())
arr = deque(map(int, input().split()))

ind = len(arr) - 1
arr_copy = deque(list(arr)[:])

e = arr.pop()
candidate = arr.pop()

while candidate >= e and ind >= 0:
    arr_copy[ind]= candidate
    print(*arr_copy, sep=" ")
    ind -= 1
    if arr:
        candidate = arr.pop()
    else:
        candidate = e
if not ind == -1:
    arr_copy[ind] = e
    print(*arr_copy, sep=" ")
