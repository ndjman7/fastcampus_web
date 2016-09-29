animals = ["dog", "cat", "monkey"]

for animal in animals:
    print(animal)           #Iterable

animals_iterator = animals.__iter__()

# animals_iterator을 하면 list_iterator가 나온다.
# animals_iterator.__next__() 를 계속하다보면 StopIteration이 나온다.
# __iter__() 대신 iter(객체)를 이용한다.

# for element in elements:
    # element
# element => elements_iterator => next

# iterable 이라 함은 => __iter__를 지닌 함수라 할 수 있고,
# iterator 라 함은   => __next__를 지닌 함수라 할 수 있다.
# ( iterable O , iterator O )

# iterable => __iter__ ( iter(___) ) => iterator 객체가 되기를 원함
# iterator => __next__ ( next(iterator)) => element... raise StopIteation()

class myrange:           #range와 같은 역할을 하는 함수를 구현해봄
    def __init__(self, n):
        self.i, self.n = 0, n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

# But next로 함수가 한 사이클을 돌면 소모되서 더 이상 사용불가능.

class myrange2:
    def __init__(self.n):
        self.n = n
    def __iter__(self):
        return myrange_iterator(self.n)

class myrange2_iterator:
    def __init__(self, n):
        self.i self.n = 0,n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

# Generator
# Generator => Iterator 이터레이터를 만들어주는 제너레이터
# yield 값을 반환하지만 그 값을 기억하고 있다. (함수 종료는 되지않음)

