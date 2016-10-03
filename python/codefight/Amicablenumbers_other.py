def amicableNumbers(n):
# 1.list comprehension으로 완전수를 구한다.
    def divs(n):
        return sum(d for d in range(1 , n) if n % d == 0)

# 2.return에 앞조건을 만족하면 뒷조건의 결과를 반환한다.
    def f(n):
        d = divs(n)
        return d != n and divs(d) == n

# 3.f(n) 0이외의 값을 가질 때 return 하게 된다.
    while not f(n):
        n+=1
    return n

print(amicableNumbers(100))
