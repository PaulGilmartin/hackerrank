import collections

T = int(input())
for test in range(T):
    no_of_cubes = int(input())
    horizontal = collections.deque(map(int, input().split()))
    vertical = collections.deque()
    if horizontal[0] > horizontal[-1]:
        vertical.append(horizontal.popleft())
    else:
        vertical.append(horizontal.pop())

    while horizontal:
        m = max(horizontal[0], horizontal[-1])
        if m > vertical[-1]:
            print("No")
            break
        else:
            if horizontal[0] > horizontal[-1]:
                vertical.append(horizontal.popleft())
            else:
                vertical.append(horizontal.pop())

    if not horizontal:
        print("Yes")
