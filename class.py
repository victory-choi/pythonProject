'''
class..!
스타크래프트...!
붕어빵 틀이다. = 변수와 함수의 집합체
'''

# 마린하나 만들자 : 공격유닛이고, 군인, 총을쏨 마린변수만들자
# name = "마린"
# hp = 40
# damage = 5
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# # 탱크하나 만들자 : 공격유닛이고, 포를쏨, 일반모드 / 시즈모드
#
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 30
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
#
# def attack(name, location, damage):
#     print("{0}이 {1}방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))
#
# attack(name, "1시", 5)
# attack(tank_name, "1시", 30)
# 아니... 탱크가 한개만 만들어지는것도 아니고 .... 그래서 class로 만드는거다.


'''
메소드
'''

# 일반유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(name))
        print("체력{0}, 공격력{1}".format(hp, damage))

# 공격유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name # 여기서 self.xxx을 통해서 자기자신에게 접근을 할수있는거야. 여기의 name은 전달받은 name을 쓴다는 얘기야
        self.hp = hp
        self.damage = damage

    def attack(self, loacation): # 메소드앞에는 항상 self를 적어준다고 생각하면됨 자기자신이다.
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, loacation, self.damage))
        # 여기서도 self.name과 self.damage는 이 클래스 자기 자신에 있는 것, 즉 위의 self.name과 damage를 쓰는거고 location 는 self가 없기 때문에 전달받은 def attack에서 전달받은걸 쓴다는 얘기다 오호... 이해됨
        # 다시 정리하면 변수에서 지정된것들은 self를 통해서 불러오고 변수로 지정하지 않고 해당 함수내에서 지정한값은 self없이 쓴다.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{}은 파괴되었습니다.".format(self.name))

# 메딕 : 의무병


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


'''
상속
'''
# 일반유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격유닛
class AttackUnit(Unit): # 상속받고 싶은 클래스를 정의해
    def __init__(self, name, hp, damage): # 위의 Class Unit과 class AttackUnit의 겹치는 부분이 있네?
        Unit.__init__(self, name, hp) # class Unit를 상속받아서 초기화 해서 class AttackUnit에 쓸수있게끔 한다.
        # self.name = name 위에것과 중복되네?
        # self.hp = hp 위에것과 중복되네?
        self.damage = damage

    def attack(self, loacation): # 메소드앞에는 항상 self를 적어준다고 생각하면됨 자기자신이다.
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, loacation, self.damage))
        # 여기서도 self.name과 self.damage는 이 클래스 자기 자신에 있는 것, 즉 위의 self.name과 damage를 쓰는거고 location 는 self가 없기 때문에 전달받은 def attack에서 전달받은걸 쓴다는 얘기다 오호... 이해됨
        # 다시 정리하면 변수에서 지정된것들은 self를 통해서 불러오고 변수로 지정하지 않고 해당 함수내에서 지정한값은 self없이 쓴다.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{}은 파괴되었습니다.".format(self.name))


'''
다중 상속
'''
# 일반유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격유닛
class AttackUnit(Unit): # 상속받고 싶은 클래스를 정의해
    def __init__(self, name, hp, damage): # 위의 Class Unit과 class AttackUnit의 겹치는 부분이 있네?
        Unit.__init__(self, name, hp) # class Unit를 상속받아서 초기화 해서 class AttackUnit에 쓸수있게끔 한다.
        # self.name = name 위에것과 중복되네?
        # self.hp = hp 위에것과 중복되네?
        self.damage = damage

    def attack(self, loacation): # 메소드앞에는 항상 self를 적어준다고 생각하면됨 자기자신이다.
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, loacation, self.damage))
        # 여기서도 self.name과 self.damage는 이 클래스 자기 자신에 있는 것, 즉 위의 self.name과 damage를 쓰는거고 location 는 self가 없기 때문에 전달받은 def attack에서 전달받은걸 쓴다는 얘기다 오호... 이해됨
        # 다시 정리하면 변수에서 지정된것들은 self를 통해서 불러오고 변수로 지정하지 않고 해당 함수내에서 지정한값은 self없이 쓴다.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{}은 파괴되었습니다.".format(self.name))

# 날수있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다 [속도 {}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 자... 여기서 보면 Flyable과 AttackUnit을 상속 받았지?
    def __init__(self, name, hp, damage, flying_speed): # 이름체력공격력은 AttackUnit을 // flying_speed은 Flyable을 받아
        AttackUnit.__init__(self, name, hp, damage) # AttackUnit 초기화
        Flyable.__init__(self, flying_speed) # Flyable 초기화

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시", )




'''
marine1 = Unit("마린", 40, 5) # self를 제외한 나머지를 넣어준다.
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
'''
'''
__init__
생성자입니당
객체(마린이나 탱크처럼 어떤클래스로부터 만들어지는 녀석들)가 만들어질때 자동으로 호출되는거임.
인스턴스 = marine1,2 tank는 Unit 클래스의 인스턴스라고함.

'''

'''
멤버변수 
클래스 내에서 정의된 변수고 그변수를 가지고 출약을 할수도있고 쓸수도있다.
        self.name = name
        self.hp = hp
        self.damage = damage
'''
'''


wraith1 = Unit("래이스", 80, 5) # 생성자를 통해서 작성한거고(init을 통해서)
print("유닛이름 : {0}, 공격력{1}".format(wraith1.name, wraith1.damage)) # 외부에서 작성한거

# 상대방의 다크아칸이 마인드 컨트롤했다고 쳐바
wraith2 = Unit("뺏은래이스", 80, 5)
wraith2.clocking = True # 외부에서 clocking이라는 추가변수를 할당함.

# if wraith1.clocking == True: # 레이스1원 clocking 변수가 없기때문에 호출을 못함~
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
    
if wraith2.clocking == True: # 객체에 추가로 변수를 외부에서 만들어서 쓸수있다.
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

'''


'''
메소드 오버라이딩 할 차례
자식클래스에서 정의한 메소드를 쓰고 싶을때 메소드를 새롭게 정의해서 쓰고싶을떄
'''


# 일반유닛
class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도] : {2}".format(self.name, location,self.speed))

# 공격유닛
class AttackUnit(Unit): # 상속받고 싶은 클래스를 정의해
    def __init__(self, name, hp, damage ,speed): # class Unit 에다가 speed 를 추가했기 때문에 speed 정보를 추가해줌
        Unit.__init__(self, name, hp, speed) # class Unit 에다가 speed 를 추가했기 때문에 speed 정보를 추가해줌
        # self.name = name 위에것과 중복되네?
        # self.hp = hp 위에것과 중복되네?
        self.damage = damage

    def attack(self, loacation): # 메소드앞에는 항상 self를 적어준다고 생각하면됨 자기자신이다.
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, loacation, self.damage))
        # 여기서도 self.name과 self.damage는 이 클래스 자기 자신에 있는 것, 즉 위의 self.name과 damage를 쓰는거고 location 는 self가 없기 때문에 전달받은 def attack에서 전달받은걸 쓴다는 얘기다 오호... 이해됨
        # 다시 정리하면 변수에서 지정된것들은 self를 통해서 불러오고 변수로 지정하지 않고 해당 함수내에서 지정한값은 self없이 쓴다.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{}은 파괴되었습니다.".format(self.name))

# 날수있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다 [속도 {}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 자... 여기서 보면 Flyable과 AttackUnit을 상속 받았지?
    def __init__(self, name, hp, damage, flying_speed): # 이름체력공격력은 AttackUnit을 // flying_speed은 Flyable을 받아
        AttackUnit.__init__(self, name, hp, 0, damage) # speed는 지상유닛 정보니까 0 을 넣어줌
        Flyable.__init__(self, flying_speed) # Flyable 초기화

    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location)
# 공중유닛을 flyable클래스의 fly함수를 통해서 날아가는거니까


# 유닛 정의
vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# 함수호출
vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# 여기서 문제가.... 지상유닛인 벌쳐는 move 함수를 써야되고 배틀크루저는 fly 함수를 써야돼
battlecruiser.move("9시")

# Unit에는 move()함수를 추가했어, AttackUnit은 지상유닛인 경우에는 그냥 move 함수가 호출이 될텐데
# FlyableAttackUnit move() 함수를 새롭게 정의해서 똑같이 정의했음



'''
pass


'''
# 건물을 만들기
# class BuildingUnit(Unit):
#     def __init__(self,name, hp, location):
#         pass # 아무것도 하지 않고 일단 넘어가라는 함수야
# # 서플라이 디팟 만들기
#
# supply_depot = BuildingUnit("서플라이 디팟", 500, "7시")

# def game_start():
#     print("[알림]새로운 게임을 시작합니다.")
# def game_over():
#     pass
#
# game_start()
# game_over()


'''
super
'''
class BuildingUnit(Unit):
    def __init__(self,name, hp, location):
        # Unit.__init__(self, name,hp,0)
        super().__init__(name,hp, 0) # self 없이쓴다. Unit class에 대해서 상속받는 부모클래스의 초기화를 할수있다. 문제는 다중상속받을때 발생.
        self.location = location


supply_depot = BuildingUnit("서플라이 디팟", 500, "7시")




'''
예외처리
'''
# print("나누기 전용 계산기")
# num1 = int(input("첫번째 숫자를 입력하세요 : "))
# num2 = int(input("첫번째 숫자를 입력하세요 : "))
# print("{0} / {1} = {2} ".format(num1, num2, int(num1 / num2)))
# ValueError: invalid literal for int() with base 10: '삼' 요런식으로 나오는걸 except 구문으로 변경

'''
예외 구문 다중처리
'''

# try:
#     print("나누기 전용 계산기")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2} ".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러가 발생했어요")
# except ZeroDivisionError as err:
#     print(err)
'''
예외 구문 다중처리
'''
# try:
#     print("나누기 전용 계산기")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫번째 숫자를 입력하세요 : "))
#     if num1 >- 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2} ".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러가 발생했어요")


'''
사용자정의 예외처리
'''

class BigNumberError(Exception):
    pass
try:
    print("나누기 전용 계산기")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("첫번째 숫자를 입력하세요 : "))
    if num1 >- 10 or num2 >= 10:
        raise BigNumberError
    print("{0} / {1} = {2} ".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러가 발생했어요")
except BigNumberError:
    print("에러가 발생했어요. 한자리 숫자만 입력하세요")
