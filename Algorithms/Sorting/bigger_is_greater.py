def lex_sort(inpt):
    if len(inpt) == 1:
        return "no answer"

    ind = len(inpt) - 2
    inpt = list(inpt)

    while ind >= 0:
        candidate = inpt[ind]
        m = ("z", float("inf"))
        for place, letter in enumerate(inpt[ind+1:]):
            if letter > candidate:
                if letter <= m[0]:
                    m = (letter, place)
        
        if m != ("z", float("inf")):
            first_half = inpt[:ind]
            to_sort = inpt[ind:]
            to_sort.pop(m[1]+1)
            second_half = [m[0]]+sorted(to_sort)
            break
        ind -= 1

    if ind < 0:
        return "no answer"
    else:
        return "".join(first_half+second_half)



t = int(input())
for i in range(t):
    print(lex_sort(input()))
