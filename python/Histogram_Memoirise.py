def memorize(func):
    __cache = {}

    def wrapper(*args):
      #  if args in __cache:
      #      return __cache[args]
      #  else:
      #      __cache[args] = func(*args)
      #      return __cache[args]
        return __cache.update({args: func(*args)}) or __cache[args]
    return wrapper

@memorize
def fibo(n):
    return n if n < 2 else fibo(n-1) + fibo(n-2)


print(fibo (10))

