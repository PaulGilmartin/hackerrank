from collections import Counter


T = int(input())

for test in range(T):
    N = int(input())
    total = 0
    nums = Counter(list(map(int, input().split())))
    for num in nums:
        if nums[num] > 1:
            total += nums[num]*(nums[num]-1)
    print(total)
