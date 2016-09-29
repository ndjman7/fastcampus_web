# 1. @property 함수를 변수처럼 만들어주는 역할
# 2. @name.setter
# 3. @classmethod Class, Instance 모두 부를 수 있다.
#    But, 첫번째 인자가 무조건 Class 자기자신
# 4. Static Method ( Class/Instance와 무관하게)

class Awesome()
    def __init__(self, name):
        self.__name = name     #__가 붙으면 내부에서만 건드려라! 하는 의미
    @property
    def name(self):
        print("Getter Called")
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def my_instance_method(self):  # Instance Method 첫 번째 인자는 무조건 self
        return self

    @classmethod
    def my_class_method(cls):
        return cls

    @staticmethod
    def my_static_method():
        return "static"
