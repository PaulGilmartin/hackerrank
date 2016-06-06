s = int(input())
ar = list(map(int, input().split()))
ind = 1
temp = ar[:]
while ind <= s - 1:
    candidate = temp[ind]
    for i, v in enumerate(temp):
        if temp[ind] <= v:
            temp.insert(i, candidate)
            temp.pop(ind+1)
            break
    ind += 1
    print(*temp, sep=" ")
