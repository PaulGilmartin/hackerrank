import collections

n = int(input())
dic = collections.OrderedDict()
for i in range(n):
    word = input()
    dic[word] = dic.get(word,0)+1

print(len(dic.keys()))
for j in dic.values():
    print(j, end =" ")
