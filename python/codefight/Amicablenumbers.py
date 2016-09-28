def properdivisors(n):
    value = 0
    result = 0
    for i in range(1,n//2+1):
        if(n%i == 0):
            value += i
    for i in range(1,value//2+1):
        if(value%i == 0):
            result += i
    if(result == n and result!=value):
        return result

def amicablenumbers(n):
    result = []
    for i in range(1 , 2000+1):
        ans = properdivisors(i)
        if(ans):
            result.append(ans)
    print(result)
    for i in result:
        if(n<=i):
            return i


print(amicablenumbers(300))

# properdivisors는 amicablenumber을 구해주는 함수이다.
# amicablenumbers 함수는 n보다 큰 amicblenumber 중 가장 작은 값을 반환해준다.
