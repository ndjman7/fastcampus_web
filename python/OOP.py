# 객체 지향 프로그래밍 (OOP; Object Oriented Programming)
# - Object - 상태(State == data), 행동(Behavior == function)
# Class, |||||| Object == Instance

# 사람 Class
# A는 객체다 ( Object )다.
# A는 사람 Class의 인스턴스 (Instance)다.

class Person:
    def __init__(self, name, age):       #초기화
        print("사람이 생성되었습니다.")
        self.name = name
        self.age = age
    def __add__(self, partner):
        print("{my_name}이 {partner_name}과 적적으로 만난다.".format(
            my_name=self.name,
            partner_name=partner.name,
        ))
    def __str__(self):
        return self.name

    def hello(self):                    #함수의 첫번째 인자로는 무조건 객체 자기 자신이 들어간다.
        print("안녕하세요, {age}살 {name} 입니다.".format(
            age=self.age,
            name=self.name,
        ))

    def meet(self, another):
        print("{my_name} 이라는 사람이 {another_name}을 만났습니다.".format(
            my_name=self.name,
            another_name=another.name,
        ))

a = Person("나대진" , 23)
b = Person("주결경" , 20)
a.meet(b)
a+b
print(a)
