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





class Memoize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print(self.cache)
            return self.cache[args]
        ret = self.func(*args)
        self.cache[args] = ret
        return ret

@Memoize
def fib(n, m):
    if n < 2:
        return 1
    if m<2:
        return 1
    return fib(n-2, m) + fib(n, m-1)
