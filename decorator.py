def calls_limit(*args, **kwargs):
    def my_decorator(func):
        count = 0
        def wrapped(*a, **kw):
            nonlocal count
            count += 1
            print(count)
            if count >= 4:
                raise RuntimeError("Allowed calls exceeded")
            return func(*a, **kw)
        count = 0
        return wrapped
    return my_decorator

@calls_limit(limit=3)
def test1(*a, **kw):
    print()

test1()
test1()
test1()
test1()



