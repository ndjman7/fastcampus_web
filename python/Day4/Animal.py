class Animal:

    def __init__(self, type, weight):
        self.type = type
        self.weight = weight

    def eat(slef, *args):

        if not args:
            print("먹이를 먹습니다.")
        else:
            print("\n".join([
                "{food}를 먹습니다".format(food=arg)
                for arg
                in args
            )]

    def swim(self):
        print("헤엄을 친다." if self.type== "fish" else "물에 빠진다.")

    def is_heavier_than(self, another):
        return self.weight > another.weight

