class Shape:

    def __init__(self, width,height):
        self.width = width
        self.height = height

    def is_bigger_than(self, another):

        if not isinstance(another, Shape):  #Type이 달라도 동작
            return "오류"
        return self.area() > another.area()

    def area(self):
        return "오류"

class Triangle(Shape):

    def area(self):                          #Method Overrding
        return self.width * self.height / 2

class Rectangle(Shape):

    def area(self):
        return self.width * self.height / 2

rec = Rectangle(10,20)
tri = Triangle(10,10)

for shape in [tri,rec]:      #다른 클래스이지만 같은 클래스를 상속받아 함수사용가능
    print(shape.area())
