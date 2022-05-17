import functools

def cached(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper

@cached
def main(array):
    result = 0
    for i in range(array):
        result += i
    return result

print(main(100000000))
print(main(100000000))



# def wraps(*args, **kwargs):
#     nonlocal cache
#     if not cache.get(args):
#         g = func(*args, **kwargs)
#         cache[args] = g
#         return g
#     else:
#         return cache[args]
#
#
# return wraps












