N = int(input())
ratings = []
for i in range(N):
    ratings.append(int(input()))

candies = [0 for i in range(N)]
candies[0] = 1

for i in range(1, N):               #this loop ensures that any child sitting to the right with a higher rating has                                           more candies
    if ratings[i] > ratings[i-1]:
        candies[i] = candies[i-1] + 1
    else:
        candies[i] = 1
#print(candies)


for j in range(N - 1, 0, -1):       #this loop ensures any child sitting to the left with a higher rating has more                                         candies
    if ratings[j - 1] > ratings[j]:
        if candies[j-1] <= candies[j]:
            candies[j - 1] = candies[j] + 1
    #else:
        #candies[j] = 1
#print(candies)
print(sum(candies))
