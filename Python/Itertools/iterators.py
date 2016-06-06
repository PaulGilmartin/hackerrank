from itertools import combinations

N = int(input())
letters = input().split()
K = int(input())

possibilities = [c for c in combinations(range(N), K)]
a_positions = {i for i in range(N) if letters[i] == "a"}

count = 0
for i in possibilities:
    if set(i)&a_positions:
        count += 1

print(count/ len(possibilities))
