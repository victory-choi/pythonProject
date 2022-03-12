

'''
스타크래프트 전반전
'''
from random import*


class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도] : {2}".format(self.name, location,self.speed))

    def damaged(self, damage): # 일반유닛도 체력있으니까 Unit class로 이동함.
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{}은 파괴되었습니다.".format(self.name))




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

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(AttackUnit):
    seize_developed = False  # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        # 시즈모드가 개발이 안되었다면, false로 return 해주고
        if Tank.seize_developed == False:
            return
        # 시즈모드가 아닐때는 시즈모드로 전환해주고
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 시즈모드일때는 시즈모드를 해제한다.
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


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
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹모드 해제상태

    def clocking(self):
        if self.clocked == True:
            print("{0} 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다")
def game_over():
    print("Player : gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")


# 게임 진행
# 게임시작
game_start()
# 마린 3마리 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
# 탱크 2마리 생성
t1 = Tank()
t2 = Tank()
# 레이스 1마리 생성

w1 = Wraith()

# 유닛 일괄 관리. 생성된 유닛 모두 append
attack_units = [] # 이 리스트에다가 담아준다.
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동하기
for unit in attack_units:
    unit.move("1시")

# 이동중 탱크시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비 ( 마린 : 스팀팩, 텡크 : 시즈모드, 레이스 : 클로킹)

for unit in attack_units:
    # 지금 만들어진 객체가 어떤 클래스의 인스턴스인지 확인. attack_units 리스트에 마린,탱크,레이스의 서로다른 클래스가 들어가있음 특정클래스의 인스턴스인지 확인하고 들어가야됨.
    # 서로 다른 유닛객체를 각각 클래스의 인스턴스인지 확인해서 각각 처리함.
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격

for unit in attack_units:
    unit.attack("1시")

# 전군 피해

for unit in attack_units:
    unit.damaged(randint(5, 20))

# 게임종료
game_over()


'''


'''

