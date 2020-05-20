from time import perf_counter

x = int(input())

cache = [None for i in range(x+1)]


def fib(n):
    if n < 2:
        return 1
    else:
        if not cache[n]:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]


start = perf_counter()
print(fib(x))
end = perf_counter()
execution_time = (end - start)
print(execution_time)
