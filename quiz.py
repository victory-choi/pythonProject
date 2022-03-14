'''사이트별로 비밀번호를 만들어주는 프로그램을 작성하세요
ex)http://naver.com
규칙1 : http://부분은 제외해라
규칙2 : 처음 만나는 점(.) 이후 부분은 제외해라
규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 e갯수 + !로 구성해라
'''


site = "http://naver.com"
my_str = site.replace("http://", "") # 규칙1
my_str = my_str[:5] # 규칙2
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(pw)



'''
당신의 학교에서는 파이썬 코딩대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했어요
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됩니다.
추첨 프로그램을 작성하세요

1. 편의상 댓글은 20명작성하고 아이디도 1~20으로 고정한다.
2. 댓글 내용과 상관없이 무작위 추첨하되 중복이 불가능하다
3. random 모듈의 shuffle과 sample을 활용한다.
# first = [1,2,3,4,5]
# print(first)
# shuffle(first)
# print(first)
# print(sample(first, 1))
'''

from random import *

comment = range(1, 21)
# print(type(comment)) range 함수임을 확인
comment = list(comment) # range -> list 함수로 변경해주고
shuffle(comment) # 섞어
print(comment) # 프린트해 사실 프린트는 필요없을것 같긴한데

'''
id = range(1, 20)
# print(type(id)) range 함수임을 확인
id = list(id) # # range -> list 함수로 변경해주고
shuffle(id) # 섞어
print(id) # 프린트해 사실 프린트는 필요없을것 같긴한데
생각해보니, 코멘트를 단사람 = id 갯수이기 때문에 이건 의미가 없지.
'''

winners = sample(comment,4)
# 변수지정을 해주자 어떻게?
# winners에다가 sample로 지정해주는데, comment 단 사람들의 id를 랜덤으로 샘플링하되 4개를 list함수로
print(winners)


# print("-- 당첨자 발표 -- \n 치킨 당첨자 : , \n 커피 당첨자 : , \n -- 축하합니다 --")
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {} ".format(winners[0]))
print("커피 당첨자 : {} ".format(winners[1:4]))
print("-- 축하합니다 --")


'''
퀴즈
당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있으 때 , 총 탑승 승객 수를 구하는 프로그램을 작성하세요

1. 승객별 은행 소요시간은 5~50분사이의 난수
2. 당신은 소요시간 5~ 15분사이의 승객만 매칭해야됨.
'''

from random import *

cnt = 0 # 총 탑승승객수
for i in range(1,51):
    time = randrange(5, 51)# 5분 ~ 50분 소요시간
    if 5<= time < 16: # # 5분 ~ 15분손님 이니 탑승 승객수 증가
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else:
        print("[X] {0}번째 손님 (소요시간 : {1}분".format(i, time))

print("총 탑승 승객 {}분".format(cnt))


'''
표준 체중을 구하는 프로그램을 작성하세요

* 표준체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

1. 표준 체중은 별도의 함수내에서 계산한다.
* 함수명 : std_weight
* 전달값 : 키(height), 성별(gender)

2. 표준체중은 소수점 둘째자리까지 표시한다.

출력예
키 175cm 남자의 표준체중은 67.38kg 입니다.

'''

def std_weight(height, gender): # 키는 m단위(실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height /100 , gender),2) # round를 통해서 소수점 2번째까지 노출해줘
print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height, gender, weight))



'''
당신은 회사에서 매주 1회 작성해야하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 - 
부서 : 
이름 : 
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하세요

1. 파일명은 '1주차.txt', '2주차.txt', ...... 와 같이 만듭니다. 

'''

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 - ".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 :")

'''
총 3대의 매물이 있습니다.
감남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년


'''


class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# 매물 정의
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)


print("총 {} 대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

'''
예외처리 퀴즈
동네에 항상 대기 손님이 있는 맛있는 치킨집이 잇습니다. 
대기 손님의 치킨 요리 시간을 줄이고자 자동주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으세요

1. 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError 로 처리할것 -> 출력메시지는 "잘못된값을 입력하였습니다."

2. 대기손님이 주문할 수 있는 총 치킨량은 10마리로 한정
치킨 소진시 사용자 정이에러 [SoldOutError]를 발생시키고 프로그램 종료 -> 출력메시지는 "재고가 소진되어 더 이상 주문을 받지 않습니다."
'''

chicken = 10
waiting = 1 # 홀안에는 현재 만석. 대기번호 1부터 시작

class SoldOutError(Exception):
    pass

try:
    while (True):
        print("[남은치킨] : {0}".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:  # 남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError # 0마리 이하일때는 ValueError 를 일으켜라
        else:
            print("[대기번호 {0}] {1}마리 주문 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except SoldOutError:
    print("재고가 소진되어 더이상 주문을 받지않습니다.")


'''
프로젝트 내에 나만의 시그니처를 만드는 모듈을 만드세요

모듈 파일명은 victory.py

import victory
victory.sign()

이 프로그램은 victory에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : tachymeter200@gmail.com

'''
