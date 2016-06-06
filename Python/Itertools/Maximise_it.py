from itertools import product

data = input().split()
K, M = int(data[0]), int(data[1])

big_list = []
for line in range(K):
    d = input().split()
    big_list.append([(int(x)**2)%M for x in d[1:]])

threes = product(*big_list)

print(max([sum(s)%M for s in threes]))


