def calls_limit(limit):
    def my_decorator(func):
        count = 0
        def wrapped(*a, **kw):
            nonlocal count
            count += 1
            if count > limit:
                raise RuntimeError("Allowed calls exceeded")
            return func(*a, **kw)
        return wrapped
    return my_decorator

@calls_limit(limit=3)
def test1(*a, **kw):
    print('Hello world')

test1()
test1()
test1()
test1()





