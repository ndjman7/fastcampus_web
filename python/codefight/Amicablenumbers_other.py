def amicableNumbers(n):
    def divs(n):
        return sum(d for d in range(1 , n) if n % d == 0)


    def f(n):
        d = divs(n)
        return d != n and divs(d) == n

    while not f(n):
        n+=1
    return n

print(amicableNumbers(100))
