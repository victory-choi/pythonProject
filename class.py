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

'''