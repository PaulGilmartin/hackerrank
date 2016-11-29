data = [int(x) for x in input().split()]
d = {0:data[0], 1:data[1]}
N = data[2]




def memoized_fib(num, memo_dict):
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)**2
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

print(memoized_fib(N-1, d))


def decorator_factory(dic):
    def memo_decorator(func):
        def new_func(m):
            if m in dic:
                return dic[m]
            else:
                dic[m] = func(m - 1) + func(m - 2)
                print(dic)
                return dic[m]
        return new_func
    return memo_decorator


@decorator_factory({0: 1, 1: 1})
def basic_fib(n):
    if n <= 1:
        return 1
    return basic_fib(n - 1) + basic_fib(n - 2)

