import collections

S = collections.Counter(input())
biggest = []
out = ""
num_chars = 0
while len(biggest) < 3:
    m = max(S.values())
    temp = sorted([(k, v) for (k, v) in S.items() if v == m])
    biggest += temp
    for k, v in temp:
        if num_chars < 3:
            out += str(k)+" "+str(v)+"\n"
            num_chars += 1
    for (k,v) in temp:
        del S[k]

print(out)
