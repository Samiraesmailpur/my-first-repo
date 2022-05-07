def cached(func):
    cache = {}
    def a(*args, **kwargs):
        nonlocal cache
        print('function started')
        if not cache.get(args):
            g = func(*args, **kwargs)
            cache[args] = g
            return g
        else:
            print('using cache')
            return cache[args]
    return a

@cached
def main(array):
    result = 0
    for i in range(array):
        result += i
    return result

print(main(100000000))
print(main(100000000))



































def cached(func):
    cache = {}
    def a(*args, **kwargs):
        nonlocal cache
        if not cache.get(args):
            g = func(*args, **kwargs)
            cache[args] = g
            return g
        else:
            return cache[args]

    return a

@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# print(fib(3))