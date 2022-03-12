class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): # 같이상속받게만들었을때 super를 쓰면 맨처음 class 만 init함수만 호출됨.
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
# super().__init__() 하면 "Unit 생성자" -> Flyable 은 타지않고 print 됨.



