"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of C = {C1, ..., CM}  valued coins,
how many ways can we make the change? The order of coins doesn’t matter.
"""


ints = [int(x) for x in input().split()]
N, M = ints[0], ints[1]
coins = [int(x) for x in input().split()]

ways = {(i, j):0 for i in range(-1, N+1) for j in range(M+1)}

for j in range(M+1):
    ways[(0, j)]  = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        ways[(i, j)]  = ways[(max(-1, i - coins[j-1]), j)] + ways[(i, j-1)]

print(ways[(N, M)])
