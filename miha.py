cache = []


def fib(x):
    if len(cache) < x:p
        [cache.append(None) for i in range(len(cache), x)]
    if x <= 2:
        return 1
    else:
        if not cache[x - 1]:
            cache[x - 1] = fib(x - 1) + fib(x - 2)
        return cache[x - 1]


print(fib())